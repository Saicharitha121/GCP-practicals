import functions_framework
import json
import logging

logging.basicConfig(level=logging.INFO)

@functions_framework.cloud_event
def on_user_create(cloud_event):
    logging.info("🔥 FIRESTORE CREATE EVENT RECEIVED")

    data = cloud_event.data or {}
    value = data.get("value", {})
    fields = value.get("fields", {})

    def get_string(field):
        return fields.get(field, {}).get("stringValue")

    def get_int(field):
        val = fields.get(field, {}).get("integerValue")
        return int(val) if val else None

    payload = {
        "document": value.get("name"),
        "name": get_string("name"),
        "email": get_string("email"),
        "role": get_string("role"),
        "exp": get_int("exp"),
    }

    logging.info(json.dumps(payload, indent=2))
    logging.info("✅ Function execution completed successfully")


# to send multiple documents to firestore automatically

# import base64
# import json
# from google.cloud import firestore
# from datetime import datetime

# db = firestore.Client(database="arundb")

# def consume_pubsub_charitha(event, context):

#     message = base64.b64decode(event['data']).decode('utf-8')
#     payload = json.loads(message)

#     event_type = payload.get("event")
#     users = payload.get("users", [])

#     batch = db.batch()

#     for user in users:
#         doc_ref = db.collection("user_activity_logs").document()
#         batch.set(doc_ref, {
#             "event": event_type,
#             "user": user,
#             "received_at": datetime.utcnow(),
#             "source": "pubsub",
#             "topic": context.resource["name"]
#         })

#     batch.commit()
#     print(f"{len(users)} users inserted into Firestore")





# to send a single document reflects to firestore automatically

#  import base64
# import json
# from google.cloud import firestore
# from datetime import datetime

# # Firestore client
# db = firestore.Client(database="arundb")

# def consume_pubsub_charitha(event, context):
#     """
#     Triggered from a Pub/Sub message
#     """

#     # Decode Pub/Sub message
#     message = base64.b64decode(event['data']).decode('utf-8')
#     payload = json.loads(message)

#     # Prepare Firestore log document
#     log_data = {
#         "event": payload.get("event"),
#         "user": payload.get("user"),
#         "received_at": datetime.utcnow(),
#         "source": "pubsub",
#         "topic": context.resource["name"]
#     }

#     # Store in Firestore (NoSQL)
#     db.collection("user_activity_logs").add(log_data)

#     print("Log stored in Firestore:", log_data)






