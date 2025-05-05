import hashlib

def generate_key_from_features(features):
    feature_str = ''.join(map(str, features))
    hash_digest = hashlib.sha256(feature_str.encode()).digest()
    return hash_digest[:16]  
