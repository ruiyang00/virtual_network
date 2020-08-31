from Serializing import Serialization
from Deserializing import Deserialization

serializtor = Serialization()
deserializtor = Deserialization()


input_str = input("Plese input text you would like to serizalizing: ")
msg = serializtor.serialize(input_str)

output_str = deserializtor.deserialize(msg)
print(bytes.fromhex(output_str).decode('utf-8'))

