from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from routes.CategoriaEquipamentoRoutes import categoria_equipamento_router
# from routes.RolesRoutes import roles_router
# from routes.UsuarioRoutes import usuario_router
from routes.UsuarioHasRoleRoutes import usuario_has_role_router
# from routes.EmprestimoRoutes import emprestimo_router
# from routes.EquipamentoRoutes import equipamento_router
from routes.AuthRoutes import auth_routes

app = FastAPI(
    title="Minha API",
    description="API de exemplo com FastAPI",
    version="1.0.0"
)


app.mount("/static", StaticFiles(directory="app/asses"), name="static")


caminho_atual = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=caminho_atual)


app.include_router(categoria_equipamento_router)
app.include_router(roles_router)
app.include_router(usuario_router)
app.include_router(usuario_has_role_router)
app.include_router(emprestimo_router)
app.include_router(equipamento_router)
app.include_router(auth_routes)



@app.get("/login", response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/administrador", response_class=HTMLResponse)
def get_administrador(request: Request):
    return templates.TemplateResponse("Admniustrador.html", {"request": request})


@app.get("/pedido-estoque", response_class=HTMLResponse)
def get_pedido_estoque(request: Request):
    return templates.TemplateResponse("pedido-estoque.html", {"request": request})
