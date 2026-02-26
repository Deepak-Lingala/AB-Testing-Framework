import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_ab_test_data(num_records=100000):
    """
    Generates synthetic e-commerce A/B testing data.
    Control group: multi-step checkout (CR ~ 10%, AOV ~$50)
    Treatment group: single-page checkout (CR ~ 10.5%, AOV ~$52)
    """
    print(f"Generating {num_records} records...")
    
    # 1. Generate User IDs
    # Mix of new and returning users (some duplicates to simulate returning traffic, though A/B tests often focus on unique visitors per session)
    # To keep it simple, I'll assume these are unique sessions. I'll have slightly fewer unique users than records.
    user_ids = [f"U{str(i).zfill(6)}" for i in range(1, int(num_records * 0.95) + 1)]
    session_user_ids = np.random.choice(user_ids, size=num_records, replace=True)
    
    # 2. Generate Timestamps (over a 2-week period)
    start_date = datetime(2026, 2, 8) # Starts 2 weeks ago
    timestamps = [start_date + timedelta(seconds=random.randint(0, 14 * 24 * 60 * 60)) for _ in range(num_records)]
    timestamps.sort() # Sort to simulate chronological traffic
    
    # 3. Assign Groups (50/50 split)
    # Using hashing on user_id to ensure consistent assignment (same user always sees same variation)
    import hashlib
    def get_group(uid):
        # Even hash -> control, odd -> treatment
        hash_val = int(hashlib.md5(uid.encode('utf-8')).hexdigest(), 16)
        if hash_val % 100 < 50: # Slight SRM? Maybe exactly 50/50. 
            return 'control'
        return 'treatment'
    
    groups = [get_group(uid) for uid in session_user_ids]
    
    # 4. Generate Landing Page & Device
    devices = np.random.choice(['Desktop', 'Mobile', 'Tablet'], p=[0.45, 0.50, 0.05], size=num_records)
    
    # Base Conversion Rates
    # Mobile tends to have lower CR than Desktop
    base_cr = {'Desktop': 0.12, 'Mobile': 0.08, 'Tablet': 0.09}
    
    # Treatment Uplift
    # Let's say treatment is better on Desktop (+10% relative) and Mobile (+5% relative)
    uplift = {'Desktop': 1.10, 'Mobile': 1.05, 'Tablet': 1.05}
    
    conversions = []
    order_values = []
    
    for i in range(num_records):
        group = groups[i]
        device = devices[i]
        
        # Calculate probability based on group and device
        prob = base_cr[device]
        if group == 'treatment':
            prob *= uplift[device]
            
        # Determine conversion
        converted = 1 if random.random() < prob else 0
        conversions.append(converted)
        
        # Calculate order value if converted
        if converted:
            # Base AOV varies by device slightly
            base_aov = {'Desktop': 65, 'Mobile': 45, 'Tablet': 55}[device]
            
            # Treatment might increase AOV slightly (e.g. easier to add upsells on one-page checkout)
            aov_multiplier = 1.05 if group == 'treatment' else 1.0
            
            # Generate log-normal distributed order value (common in e-commerce)
            # mean of underlying normal distribution
            mu = np.log(base_aov * aov_multiplier)
            sigma = 0.5 # variance
            
            ov = np.round(np.random.lognormal(mean=mu, sigma=sigma), 2)
            # Cap extreme outliers and ensure minimum order value
            ov = max(5.0, min(ov, 500.0))
            order_values.append(ov)
        else:
            order_values.append(np.nan)
            
    # Compile into DataFrame
    df = pd.DataFrame({
        'session_id': [f"S{str(i).zfill(6)}" for i in range(1, num_records + 1)],
        'user_id': session_user_ids,
        'timestamp': timestamps,
        'group': groups,
        'landing_page': ['checkout_step_1' if g == 'control' else 'checkout_one_page' for g in groups],
        'device': devices,
        'converted': conversions,
        'order_value': order_values
    })
    
    # Add some realistic data quality issues (optional, but good for robust analysis)
    # A tiny bit of missing device info
    missing_indices = np.random.choice(df.index, size=int(num_records * 0.001), replace=False)
    df.loc[missing_indices, 'device'] = np.nan
    
    print(f"Data generation complete. Control: {sum((df['group'] == 'control'))}, Treatment: {sum((df['group'] == 'treatment'))}")
    print(f"Overall CR: {df['converted'].mean():.4f}")
    
    df.to_csv('ab_test_data.csv', index=False)
    print("Saved to 'ab_test_data.csv'")

if __name__ == "__main__":
    import os
    print(f"Current working directory: {os.getcwd()}")
    generate_ab_test_data()
