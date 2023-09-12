# Claude 2 API ( Unofficial )

This project provides an unofficial API for Claude AI from Anthropic, allowing users to access and interact with Claude AI and trying out experiments with the same.


Current Version == 1.1.5


> The python package that returns response of  [Claude 2](https://claude.ai/)  through value of session cookies.

**Please exercise caution and use this package responsibly.**

## Installation

To use the Claude AI Unofficial API, you can either clone the GitHub repository or directly download the Python file.

Terminal :
```
$ pip install claude2

```

or

Clone the repository:
```
git clone [https://github.com/Nipun1212/Claude_api.git]
```

<br>

## Authentication
> **Warning** Do not expose the `_SessionKey=` 
1. Visit [https://claude.ai/](https://claude.ai/)
2. F12 for console
3. Session: Network → Request Header → Cookie header → Copy the value of  `__SessionKey=` cookie.

 ![Screenshot (8)](https://github.com/KoushikNavuluri/Claude-API/assets/103725723/355971e3-f46c-47fc-a3cf-008bb55bb4c6)


Note that while I referred to `__SessionKey=` value as an API key for convenience, it is not an officially provided API key. 
Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

<br>

## Usage 

```python
from claude import Claude
cookie = "sessionKey=..."
claude = Claude(cookie)
```

After initalising the claude object, it automatically takes your most recent conversation, without facing the hassle of choosing your conversation ID, allowing you to simply chat with the model.

```python
prompt = "Hello, Claude!"
response=claude.get_answer(prompt)
print(response)
```



## Create New Chat
If you want to start a new convewrsation you can just run 
```python
claude.create_new_conversation()
```
and it automatically updates your conversation ID, allowing you yo easily chat with the model again using
```python
prompt = "Hello, Claude!"
response=claude.get_answer(prompt)
print(response)
```


## Disclaimer

This project provides an unofficial API for Claude AI and is not affiliated with or endorsed by Claude AI or Anthropic. Use it at your own risk.
The package was created to support developers in testing functionalities due to delays in the official Claude API package. However, it should not be misused or abused. Please be cautious and refer to the Readme for more information.
  
<br><br>
  
*Copyright (c) 2023  Nipun Bhatia*<br>


Please refer to the official Claude AI documentation[https://claude.ai/docs] for more information on how to use Claude AI.
        














