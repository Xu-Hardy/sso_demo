from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse
import requests
import os

app = FastAPI()

# 配置
CLIENT_ID = ""
CLIENT_SECRET = ""
AUTHORIZATION_BASE_URL = ''
TOKEN_URL = ''
REDIRECT_URI = ''
SESSION_URI = ''


@app.get("/")
def read_root():
    return {"message": "Hello Oauth"}


@app.get("/login")
def login():
    # 构建授权 URL，并将用户重定向到授权服务器
    authorization_url = (
        f"{AUTHORIZATION_BASE_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    )
    return RedirectResponse(authorization_url)


@app.get("/callback")
def callback(request: Request):
    # 从请求中获取授权码
    code = request.query_params.get('code')
    if not code:
        raise HTTPException(status_code=400, detail="Missing authorization code")

    # 交换授权码获取访问令牌
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    try:
        token_response = requests.post(TOKEN_URL, data=token_data)
        token_response.raise_for_status()
        token_json = token_response.json()
        access_token = token_json.get('access_token')
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 返回访问令牌或用户信息给前端
    return JSONResponse(content={"access_token": access_token})

@app.get("/user_info")
def user_info(request: Request):
    # 从请求中获取访问令牌
    access_token = request.headers.get('Authorization')
    if not access_token:
        raise HTTPException(status_code=401, detail="Missing access token")

    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        user_info_response = requests.get(SESSION_URI, headers=headers)
        user_info_response.raise_for_status()
        user_info_json = user_info_response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 返回用户信息给前端
    return JSONResponse(content=user_info_json)



if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8080)
