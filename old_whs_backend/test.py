import requests

API_BASE_URL = "http://localhost:5001"

def test_login(username, password):
    response = requests.post(f"{API_BASE_URL}/login", data={"username": username, "password": password})
    
    if response.status_code == 200:
        print("Login réussi")
    else:
        print("Erreur lors de la connexion:", response.status_code, response.text)

def main():
    test_login("test1", "0000")

if __name__ == "__main__":
    main()
