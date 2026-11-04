import jwt
import secrets
from datetime import datetime, timezone, timedelta

# Step 1: Generate a secret key
SECRET_KEY = secrets.token_hex(32)

# Step 2: Create the JWT payload
payload = {
    "user_id": 101,
    "role": "customer",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}

# Step 3: Generate the JWT token
token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print("\nGenerated JWT:")
print(token)


# Step 4: Decode and verify the token
try:
    decoded_data = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )

    print("\nDecoded JWT:")
    print(decoded_data)

    print("\nUser ID:", decoded_data["user_id"])
    print("User Role:", decoded_data["role"])

except jwt.ExpiredSignatureError:
    print("\nToken expired! Please login again.")

except jwt.InvalidTokenError:
    print("\nInvalid token!")


# Step 5: Generate an already-expired token
expired_payload = {
    "user_id": 101,
    "role": "customer",
    "exp": datetime.now(timezone.utc) - timedelta(minutes=-1)
}

expired_token = jwt.encode(
    expired_payload,
    SECRET_KEY,
    algorithm="HS256"
)

print("\nExpired JWT:")
print(expired_token)


# Step 6: Try decoding the expired token
try:
    expired_data = jwt.decode(
        expired_token,
        SECRET_KEY,
        algorithms=["HS256"]
    )

    print("\nDecoded data:", expired_data)

except jwt.ExpiredSignatureError:
    print("\nToken expired! Please login again.")

except jwt.InvalidTokenError:
    print("\nInvalid token!")