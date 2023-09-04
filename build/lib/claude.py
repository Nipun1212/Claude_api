from curl_cffi import requests
import json
import os
import uuid


class Claude:


    def __init__(self, cookie) -> None:
        self.cookies=cookie
        self.organisation_uuid=self.get_organisation_uuid()
        self.conversation_uuid=''
        self.get_conversation_uuid()
        



    def get_organisation_uuid(self):
        uuid=''

        url = 'https://claude.ai/api/organizations'

        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://claude.ai/chats',
            'Content-Type': 'application/json',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'keep-alive',
            'Cookie': f'{self.cookies}'
        }

        response = requests.get(url, headers=headers,impersonate="chrome110")

        if response.status_code == 200:
            data = response.json()
            uuid=data[0]['uuid']

            # Process the response data and analyze the chatbot's API behavior
            # Extract relevant information from the data and observe any patterns
        else:
            # Handle the case when the request is not successful
            print('Request failed with status code:', response.status_code)
            print('Please check the cookies you have entered.')
            print('If they are correct then Claude might be down')
        
        return uuid
    

    def get_random_uuid(self) -> str:

        random_uuid=uuid.uuid4()
        new_uuid=str(random_uuid)
        return new_uuid
    
    def get_conversation_uuid(self):

        url = f'https://claude.ai/api/organizations/{self.organisation_uuid}/chat_conversations'

        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://claude.ai/chats',
            'Content-Type': 'application/json',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'keep-alive',
            'Cookie': f'{self.cookies}'
        }

        response = requests.get(url, headers=headers,impersonate="chrome110")

        if response.status_code == 200:
            conversation_history = response.json()
            if(conversation_history==[]):
                print('No old conversations, creating a new one')
                self.create_new_conversation()
                
            else:
                print('Found old conversations, using the most recent one')
                most_receent_conversation=conversation_history[-1]
                self.conversation_uuid=most_receent_conversation['uuid']
                
                
            

            # Process the response data and analyze the chatbot's API behavior
            # Extract relevant information from the data and observe any patterns
        else:
            # Handle the case when the request is not successful
            print('Request failed with status code:', response.status_code)
            print('Please check the cookies you have entered.')
            print('If they are correct then Claude might be down')
        
        return

        

    
    def create_new_conversation(self) -> None:

        url = f"https://claude.ai/api/organizations/{self.organisation_uuid}/chat_conversations"
        conversation_uuid = self.get_random_uuid()

        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://claude.ai/chats',
            'Content-Type': 'application/json',
            'Origin': 'https://claude.ai',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Cookie': f'{self.cookies}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }


        payload= json.dumps({"uuid": conversation_uuid, "name": ""})

        response = requests.post(url,data=payload, headers=headers,impersonate="chrome110")

        if response.status_code == 201:
            data=response.json()

            self.conversation_uuid= data['uuid']
            print('New Conversation Created')
            

            
        
        else:
            print('Request failed with status code:', response.status_code)
            print('Unable to create a new conversation please try again')

        
    
    def get_answer(self,prompt):

        url='https://claude.ai/api/append_message'

        payload=json.dumps({'attachments': [],
                    'completion': { 'incremental': 'true',
                    'model': "claude-2",
                    'prompt': f'{prompt}',
                    'timezone': "Asia/Singapore"},
                    "organization_uuid": f"{self.organisation_uuid}",
                    "conversation_uuid": f"{self.conversation_uuid}",
                    'text': f'{prompt}'})
        
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'text/event-stream, text/event-stream',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://claude.ai/chats',
            'Content-Type': 'application/json',
            'Origin': 'https://claude.ai',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Cookie': f'{self.cookies}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }

        response = requests.post(url, headers=headers, data=payload,impersonate="chrome110")

        lines = response.text.split('\n')

        # Extract completion values from lines starting with 'data:'
        completions = ''
        for line in lines:
            if line.startswith('data:'):
                json_str = line.replace('data:', '').strip()
                json_obj = json.loads(json_str)
                completion = json_obj.get('completion')
                if completion is not None:
                    completions+=completion

        # Print the extracted completion values
        # print(completions)
        return completions


    








    





    

    






            



