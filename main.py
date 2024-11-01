import boto3, json, math

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')


def report_breakdown(user_name: str, product_name: str, product_status: str):
    # DB에 저장
    print("##############################")
    print("아래 고객 접수 내용을 DB에 저장합니다.")
    print(f"고객 이름: {user_name}")
    print(f"제품 이름: {product_name}")
    print(f"제품 증상: {product_status}")
    print("##############################")
    print()
    return


tool_list = [
    {
        "toolSpec": {
            "name": "report_breakdown",
            "description": "제품 고장 접수 내용을 DB 에 저장",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "user_name": {
                            "type": "string",
                            "description": "접수 사용자 이름"
                        },
                        "product_name": {
                            "type": "string",
                            "description": "고장난 제품의 이름"
                        },
                        "product_status": {
                            "type": "string",
                            "description": "고장난 제품의 상태"
                        },

                    },
                    "required": ["user_name", "product_name", "product_status"]
                }
            }
        }
    }
]

message_list = []


def clear_history():
    message_list.clear()


def invoke_bedrock(message: str):
    initial_message = {
        "role": "user",
        "content": [
            {"text": message}
        ],
    }

    message_list.append(initial_message)

    response = bedrock.converse(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        messages=message_list,
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
        toolConfig={
            "tools": tool_list
        },
        system=[{"text": "너는 고장접수를 하는 상담봇입니다. 필요한 정보는 사용자의 이름, 제품 이름, 제품 증상입니다. 전달받은 데이터는 DB에 저장을 해야 합니다."}]
    )

    response_message = response['output']['message']
    message_list.append(response_message)
    return response_message


def manage_response_content(response_content):
    for content_block in response_content:
        if 'text' in content_block:
            print(f"assistance:")
            print(content_block['text'] + "\n")

        if 'toolUse' in content_block:
            tool_use_block = content_block['toolUse']
            tool_use_name = tool_use_block['name']

            if tool_use_name == 'report_breakdown':
                user_name = tool_use_block['input']['user_name'];
                product_name = tool_use_block['input']['product_name'];
                product_status = tool_use_block['input']['product_status'];

                report_breakdown(user_name, product_name, product_status)

