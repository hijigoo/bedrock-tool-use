from main import *

print("# Case1: 필요한 내용을 한 번에 애기하는 시나리오")

clear_history()
user_message = "상담 접수해줘"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "김기철이고 제품 이름은 비스포크에다가 지금 불이 안들어와"
print(f"user: \n{user_message}\n"
      f"")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))
print()

print("# Case2: 필요한 내용을 하나씩 애기하는 시나리오")

clear_history()
user_message = "상담 접수해줘"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "김기철이야"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "제품 이름은 비스포크야."
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
assistance_message = response["content"][0]["text"]
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "냉장고에 불이 안들어와"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))
print()

print("# Case3: 필요한 내용을 중간에 수정해서 얘기하는 시나리오")

clear_history()
user_message = "상담 접수해줘"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "홍기철이야"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "제품 이름은 비스포크야."
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "아 내 이름은 김기철이야"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

user_message = "냉장고에 불이 안들어와"
print(f"user: \n{user_message}\n")
response = invoke_bedrock(user_message)
manage_response_content(response["content"])
# print(json.dumps(response, indent=4, ensure_ascii=False))

print()
