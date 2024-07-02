from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dados de exemplo: Lista de países e seus códigos de discagem
countries = {
     "Angola": "+224",
    "Brazil": "+55",
    "United States": "+1",
    "Canada": "+1",
    "France": "+33",
    "Germany": "+49",
    "India": "+91",
    "Japan": "+81",
    # Adicione mais países conforme necessário
}

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à minha primeira API!"}

@app.get("/countries/")
def get_countries():
    return countries

@app.get("/countries/{country_name}")
def get_country_code(country_name: str):
    code = countries.get(country_name)
    if code:
        return {"country": country_name, "code": code}
    else:
        raise HTTPException(status_code=404, detail="Country not found")


 #Nome:Ananias Tómas
  #N-20220663