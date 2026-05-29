import streamlit as st
import json
import os
import urllib.parse
import base64
import textwrap
from PIL import Image

# 1. Configuração Inicial da Página (Modo Wide + Título)
st.set_page_config(
    page_title="Dinara Soares Beauty",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Carregar Dados Dinamicamente do JSON
def carregar_dados():
    with open("dados.json", "r", encoding="utf-8") as file:
        return json.load(file)

try:
    dados = carregar_dados()
except Exception as e:
    st.error(f"Erro ao carregar o arquivo dados.json: {e}")
    st.stop()

# 3. Funções Utilitárias
def gerar_link_whatsapp(telefone, mensagem):
    """Gera um link wa.me válido com mensagem codificada para o WhatsApp."""
    texto_codificado = urllib.parse.quote(mensagem)
    return f"https://wa.me/{telefone}?text={texto_codificado}"

def carregar_imagem_base64(caminho_imagem):
    """Carrega uma imagem local e retorna seu conteúdo codificado em Base64."""
    if os.path.exists(caminho_imagem):
        with open(caminho_imagem, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    return ""

def render_markdown(html_str):
    """Renderiza HTML no Streamlit de forma robusta removendo quebras de linha que causam falsos blocos de código."""
    lines = html_str.split("\n")
    if lines and not lines[0].strip():
        lines = lines[1:]
    if lines and not lines[-1].strip():
        lines = lines[:-1]
    
    # Encontra a indentação mínima de linhas não vazias
    non_empty_lines = [line for line in lines if line.strip()]
    if non_empty_lines:
        min_indent = min(len(line) - len(line.lstrip()) for line in non_empty_lines)
        dedented_lines = [line[min_indent:] if len(line) >= min_indent else line.lstrip() for line in lines]
        html_str = " ".join(dedented_lines)
    else:
        html_str = " ".join(lines)
        
    st.markdown(html_str, unsafe_allow_html=True)

# 4. Estilos CSS Premium (Editorial Dark Mode & Satin Gold)
render_markdown("""
<style>
    /* Importação de Fontes Editoriais de Alta Moda */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=Tenor+Sans&display=swap');
    
    /* Reset de Fundo e Layout Geral (Radial Gradient Carvão e Chocolate Escuro) */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Tenor Sans', sans-serif !important;
        background: radial-gradient(circle at center, #1B1310 0%, #080706 100%) !important;
        color: #FAF7F2 !important;
    }
    
    /* Configuração e Alinhamento de Títulos Globais */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cormorant Garamond', serif !important;
        color: #FAF7F2 !important;
        font-weight: 300 !important;
        letter-spacing: 1px !important;
    }
    
    /* Título Principal com Letras Espaçadas */
    .editorial-title {
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 3.5rem !important;
        font-weight: 300 !important;
        letter-spacing: 3px !important;
        line-height: 1.1;
        color: #FAF7F2 !important;
        margin-bottom: 10px;
    }
    
    .editorial-subtitle {
        font-family: 'Tenor Sans', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #C5A880;
        font-size: 0.85rem;
    }

    /* Divisor de Ouro Ultrafino */
    .gold-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(230, 194, 128, 0.4), transparent);
        margin: 25px 0;
    }

    /* Barra Lateral Personalizada (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #080706 !important;
        border-right: 1px solid rgba(230, 194, 128, 0.1) !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #FAF7F2 !important;
    }

    /* Customização dos Radio Buttons da Sidebar para Menu Limpo */
    div[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] {
        padding: 10px 14px !important;
        background-color: transparent !important;
        border-radius: 0px !important;
        border-left: 2px solid transparent !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-testid="stSidebarUserContent"] label[data-baseweb="radio"]:hover {
        background-color: rgba(230, 194, 128, 0.03) !important;
        border-left: 2px solid rgba(230, 194, 128, 0.4) !important;
    }
    
    /* Esconder o círculo nativo do radio para parecer lista de links */
    div[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] div[role="presentation"] {
        display: none !important;
    }
    
    /* Estilo do Texto do Menu */
    div[data-testid="stSidebarUserContent"] .st-ae {
        font-family: 'Tenor Sans', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-size: 0.85rem !important;
        color: #A09386 !important;
    }
    
    /* Link Ativo */
    div[data-testid="stSidebarUserContent"] label[data-baseweb="radio"][aria-checked="true"] {
        border-left: 2px solid #E6C280 !important;
        background-color: rgba(230, 194, 128, 0.06) !important;
    }
    
    div[data-testid="stSidebarUserContent"] label[data-baseweb="radio"][aria-checked="true"] .st-ae {
        color: #E6C280 !important;
        font-weight: 500 !important;
    }

    /* Botão Base do Streamlit e stLinkButton estilizado */
    div.stButton > button, div[data-testid="stLinkButton"] a {
        background-color: transparent !important;
        color: #E6C280 !important;
        border: 1px solid rgba(230, 194, 128, 0.5) !important;
        border-radius: 0px !important; /* Cantos retos clássicos de revista */
        font-family: 'Tenor Sans', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-size: 0.75rem !important;
        padding: 10px 24px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        width: 100%;
        text-align: center;
        display: inline-flex !important;
        align-items: center;
        justify-content: center;
        text-decoration: none !important;
    }
    
    div.stButton > button:hover, div[data-testid="stLinkButton"] a:hover {
        background-color: #E6C280 !important;
        color: #090807 !important;
        border-color: #E6C280 !important;
        box-shadow: 0 0 15px rgba(230, 194, 128, 0.15) !important;
        transform: translateY(-1px);
    }

    /* Botão de Link customizado em HTML */
    .luxury-btn {
        background-color: transparent !important;
        color: #E6C280 !important;
        border: 1px solid rgba(230, 194, 128, 0.5) !important;
        text-decoration: none !important;
        font-family: 'Tenor Sans', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-size: 0.75rem !important;
        padding: 10px 24px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    .luxury-btn:hover {
        background-color: #E6C280 !important;
        color: #090807 !important;
        border-color: #E6C280 !important;
        box-shadow: 0 0 15px rgba(230, 194, 128, 0.15) !important;
    }

    /* Cards de Vidro Obsidiana (Glassmorphism Escuro) */
    .luxury-card {
        background: rgba(18, 15, 14, 0.6);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(230, 194, 128, 0.12);
        border-radius: 0px; /* Sem cantos arredondados para uma estética limpa */
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .luxury-card:hover {
        border-color: rgba(230, 194, 128, 0.4);
        box-shadow: 0 15px 50px rgba(230, 194, 128, 0.08);
        transform: translateY(-2px);
    }

    /* Customização das Tabs do Streamlit */
    div[data-testid="stTabBar"] {
        border-bottom: 1px solid rgba(230, 194, 128, 0.1) !important;
        gap: 15px !important;
    }
    
    div[data-testid="stTabBar"] button {
        font-family: 'Tenor Sans', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        color: #A09386 !important;
        background-color: transparent !important;
        border: none !important;
        font-size: 0.8rem !important;
        padding: 12px 20px !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-testid="stTabBar"] button[aria-selected="true"] {
        color: #E6C280 !important;
        border-bottom: 2px solid #E6C280 !important;
        font-weight: 500 !important;
    }

    /* Efeito de Filtro Escuro para o Mapa do Google */
    iframe {
        filter: invert(90%) hue-rotate(180deg) brightness(88%) contrast(100%) sepia(10%) saturate(110%);
        border: 1px solid rgba(230, 194, 128, 0.15) !important;
        border-radius: 0px !important;
    }

    /* Animação de Entrada dos Conteúdos */
    .fade-in {
        animation: fadeInEffect 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes fadeInEffect {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .footer {
        text-align: center;
        padding: 40px 0;
        font-size: 0.9rem;
        color: #8C8070;
        border-top: 1px solid rgba(230, 194, 128, 0.15);
        margin-top: 60px;
    }
    
    /* Limitar tamanho máximo e aplicar moldura no player de vídeo do Streamlit */
    video[data-testid="stVideo"], .stVideo {
        max-width: 320px !important;
        width: 100% !important;
        height: auto !important;
        margin: 10px auto 30px auto !important;
        border: 1px solid rgba(230, 194, 128, 0.2) !important;
        padding: 10px !important;
        background: rgba(12,11,10,0.4) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
        display: block !important;
    }
</style>
""")

# Prepara a imagem do logo em base64 para uso inline
logo_b64 = carregar_imagem_base64("assets/logo.jpeg")

# 5. Configuração da Barra Lateral (Sidebar)
with st.sidebar:
    st.write("")
    if logo_b64:
        render_markdown(f"""
        <div class="fade-in" style="text-align: center; padding: 15px 0 10px 0;">
            <img src="data:image/jpeg;base64,{logo_b64}" style="width: 85%; max-width: 160px; filter: contrast(1.05) brightness(0.95);">
        </div>
        """)
    else:
        st.markdown(f"<div style='text-align: center; padding: 20px 0;'><h2 style='font-family: \"Cormorant Garamond\", serif; font-size: 2.2rem; letter-spacing: 2px;'>{dados['salao']['nome']}</h2></div>", unsafe_allow_html=True)
        
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'><span style='font-family: \"Cormorant Garamond\", serif; font-style: italic; font-size: 1.1rem; color: #A09386;'>Beleza e Cuidados</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
    
    # Navegação do App
    paginas = {
        "Essência": "sobre",
        "Serviços": "servicos",
        "Catálogo de produtos": "lojinha",
        "Localização / Contato": "contato"
    }
    pagina_selecionada = st.radio(
        "Navegação",
        list(paginas.keys()),
        label_visibility="collapsed"
    )
    
    st.markdown("<div class='gold-divider' style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    
    # Horários de Funcionamento na Sidebar
    st.markdown("<p style='font-family: \"Tenor Sans\", sans-serif; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: #FAF7F2; margin-bottom: 10px;'>Horários</p>", unsafe_allow_html=True)
    for horario in dados['contato']['horarios']:
        st.markdown(f"<p style='font-size: 0.85rem; color: #A09386; margin: 4px 0;'>{horario}</p>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    # Botão de Ação Rápida WhatsApp na Sidebar
    link_geral_whatsapp = gerar_link_whatsapp(
        dados['contato']['telefone_whatsapp'],
        dados['contato']['mensagem_agendamento']
    )
    st.link_button("Reservar Horário", link_geral_whatsapp)

# 6. Roteamento das Páginas
secao = paginas[pagina_selecionada]

# ==========================================
# SEÇÃO 1: SOBRE NÓS / A ESSÊNCIA
# ==========================================
if secao == "sobre":
    # Header Principal da Home
    render_markdown(f"""
    <div class='fade-in' style='text-align: center; padding: 40px 0 20px 0;'>
        <span class='editorial-subtitle'>Estética e Cuidados</span>
        <h1 class='editorial-title'>{dados['salao']['nome']}</h1>
        <div class='gold-divider'></div>
        <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.45rem; color: #A09386; max-width: 800px; margin: 0 auto; line-height: 1.6;">
            "{dados['salao']['slogan']}"
        </p>
    </div>
    """)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Bloco "A Essência" (Texto + Imagem de Capa)
    col_sobre_1, col_sobre_2 = st.columns([11, 9])
    with col_sobre_1:
        render_markdown(f"""
        <div class='fade-in' style='padding-right: 20px; margin-top: 15px;'>
            <span style="font-family: 'Tenor Sans', sans-serif; text-transform: uppercase; letter-spacing: 2px; color: #C5A880; font-size: 0.8rem; display: block; margin-bottom: 10px;">A Essência</span>
            <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.6rem; font-weight: 300; margin: 0 0 25px 0; color: #FAF7F2; line-height: 1.2;">Revelando o brilho único de cada detalhe.</h2>
            <p style="font-family: 'Cormorant Garamond', serif; font-size: 1.35rem; line-height: 1.8; color: #FAF7F2; text-align: justify; font-style: italic; font-weight: 300; border-left: 2px solid #E6C280; padding-left: 25px; margin-bottom: 30px;">
                {dados['salao']['sobre_curto']}
            </p>
        </div>
        """)
    with col_sobre_2:
        if logo_b64:
            render_markdown(f"""
            <div class='fade-in' style='border: 1px solid rgba(230, 194, 128, 0.2); padding: 25px; background: rgba(12,11,10,0.4); text-align: center;'>
                <img src="data:image/jpeg;base64,{logo_b64}" style="width: 100%; max-width: 300px; filter: contrast(1.05) brightness(0.95);">
            </div>
            """)
            
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Grid de Valores (Estilo Editorial Numerado)
    st.markdown("<div style='text-align: center; margin-bottom: 30px;'><span class='editorial-subtitle'>Nossa Filosofia</span></div>", unsafe_allow_html=True)
    cols_valores = st.columns(2)
    for i, valor in enumerate(dados['salao']['valores']):
        with cols_valores[i % 2]:
            render_markdown(f"""
            <div class='luxury-card fade-in'>
                <span style="font-family: 'Cormorant Garamond', serif; font-size: 3.2rem; font-style: italic; color: #E6C280; font-weight: 300; display: block; line-height: 1;">0{i+1}.</span>
                <h4 style="font-family: 'Tenor Sans', sans-serif; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; font-size: 1.05rem; color: #FAF7F2; border-bottom: 1px solid rgba(230, 194, 128, 0.1); padding-bottom: 10px; margin-bottom: 15px;">{valor['titulo']}</h4>
                <p style='font-size: 0.95rem; line-height: 1.6; color: #A09386; font-family: "Tenor Sans", sans-serif; text-align: justify;'>{valor['descricao']}</p>
            </div>
            """)

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Subseção de Transparência e Qualidade de Marcas
    st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
    render_markdown(f"""
    <div class='fade-in' style='text-align: center; max-width: 800px; margin: 0 auto; padding-bottom: 30px;'>
        <span class='editorial-subtitle'>Transparência & Excelência</span>
        <h2 style="font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; font-weight: 300; margin: 15px 0; color: #FAF7F2;">Com que Cuidamos de Você</h2>
        <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.2rem; color: #A09386; line-height: 1.6;">
            {dados['salao']['transparencia_texto']}
        </p>
    </div>
    """)
    
    cols_marcas = st.columns(len(dados['marcas']))
    for idx, marca in enumerate(dados['marcas']):
        marca_img_b64 = carregar_imagem_base64(marca['logo'])
        with cols_marcas[idx]:
            render_markdown(f"""
            <div class='luxury-card fade-in' style='text-align: center; height: 100%;'>
                <div style="height: 100px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <img src="data:image/jpeg;base64,{marca_img_b64}" style="max-height: 80px; max-width: 130px; object-fit: contain;">
                </div>
                <h4 style='font-family: "Tenor Sans", sans-serif; text-transform: uppercase; letter-spacing: 2px; font-size: 0.95rem; color: #FAF7F2; margin-top: 20px; border-bottom: 1px solid rgba(230, 194, 128, 0.1); padding-bottom: 10px; margin-bottom: 15px;'>{marca['nome']}</h4>
                <p style='font-family: "Cormorant Garamond", serif; font-style: italic; font-size: 1.1rem; color: #A09386; margin-top: 12px; line-height: 1.5; text-align: center;'>{marca['descricao']}</p>
            </div>
            """)

# ==========================================
# SEÇÃO 2: SERVIÇOS & PORTFÓLIO
# ==========================================
elif secao == "servicos":
    render_markdown("""
    <div class='fade-in' style='text-align: center; padding: 30px 0;'>
        <span class='editorial-subtitle'>A Arte em Movimento</span>
        <h1 class='editorial-title'>Portfólio & Serviços</h1>
        <div class='gold-divider'></div>
    </div>
    """)
    
    # Galeria e Portfólio
    st.markdown("<div style='margin-bottom: 20px;'><h3 style='font-family: \"Cormorant Garamond\", serif; font-size: 2rem; border-bottom: 1px solid rgba(230, 194, 128, 0.1); padding-bottom: 10px;'>Portfólio</h3></div>", unsafe_allow_html=True)
    
    for item in dados['portfolio']:
        st.markdown(f"<h5 style='font-family: \"Tenor Sans\", sans-serif; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.95rem; color: #FAF7F2;'>{item['titulo']}</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#A09386; font-family: \"Cormorant Garamond\", serif; font-style: italic; font-size: 1.15rem; margin-bottom: 20px;'>{item['descricao']}</p>", unsafe_allow_html=True)
        
        if item['tipo'] == "imagem":
            # Exibição de Antes e Depois Lado a Lado com bordas douradas elegantes
            antes_b64 = carregar_imagem_base64(item['antes'])
            depois_b64 = carregar_imagem_base64(item['depois'])
            
            render_markdown(f"""
            <div class='fade-in' style='display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-bottom: 30px;'>
                <div>
                    <div style='border: 1px solid rgba(230, 194, 128, 0.15); padding: 10px; background: rgba(12,11,10,0.3); text-align: center;'>
                        <img src="data:image/jpeg;base64,{antes_b64}" style="width: 100%; height: 480px; object-fit: contain;">
                    </div>
                    <p style='text-align: center; font-family: "Tenor Sans", sans-serif; text-transform: uppercase; letter-spacing: 2px; font-size: 0.75rem; color: #A09386; margin-top: 10px;'>Antes</p>
                </div>
                <div>
                    <div style='border: 1px solid rgba(230, 194, 128, 0.3); padding: 10px; background: rgba(12,11,10,0.3); text-align: center;'>
                        <img src="data:image/jpeg;base64,{depois_b64}" style="width: 100%; height: 480px; object-fit: contain;">
                    </div>
                    <p style='text-align: center; font-family: "Tenor Sans", sans-serif; text-transform: uppercase; letter-spacing: 2px; font-size: 0.75rem; color: #E6C280; font-weight: bold; margin-top: 10px;'>Depois (Transformação)</p>
                </div>
            </div>
            """)
            
        elif item['tipo'] == "video":
            # Exibição de Vídeo com tamanho e moldura controlados via CSS global
            st.video(item['video_url'], autoplay=True, loop=True, muted=True)
            
        st.markdown("<div class='gold-divider' style='margin: 40px 0;'></div>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='margin-bottom: 25px;'><h3 style='font-family: \"Cormorant Garamond\", serif; font-size: 2rem; border-bottom: 1px solid rgba(230, 194, 128, 0.1); padding-bottom: 10px;'>Menu de Serviços</h3></div>", unsafe_allow_html=True)
    
    # Tabela de Serviços Organizada em Tabs (Menu Michelin Style)
    tabs_categorias = st.tabs([cat["categoria"] for cat in dados["categorias_servicos"]])
    
    for idx_cat, cat in enumerate(dados["categorias_servicos"]):
        with tabs_categorias[idx_cat]:
            render_markdown("<div class='fade-in' style='padding-top: 15px;'>")
            for item in cat["itens"]:
                msg_servico = f"Olá! Vim pelo aplicativo e gostaria de agendar o serviço '{item['nome']}' (R$ {item['preco']:.2f})."
                link_whatsapp = gerar_link_whatsapp(
                    dados['contato']['telefone_whatsapp'],
                    msg_servico
                )
                
                # Renderiza o item de serviço em um layout limpo de alta costura com o botão flex
                render_markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed rgba(230, 194, 128, 0.15); padding: 18px 0;">
                    <div style="max-width: 75%;">
                        <span style="font-family: 'Tenor Sans', sans-serif; text-transform: uppercase; letter-spacing: 1.5px; font-size: 1rem; color: #FAF7F2; font-weight: 400;">{item['nome']}</span>
                        <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.05rem; color: #A09386; margin-top: 5px; margin-bottom: 0; line-height: 1.4; text-align: justify;">
                            {item['descricao']}
                        </p>
                    </div>
                    <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 8px; min-width: 130px;">
                        <span style="font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; font-weight: 500; color: #E6C280;">R$ {item['preco']:.2f}</span>
                        <a href="{link_whatsapp}" target="_blank" class="luxury-btn" style="padding: 6px 16px !important; font-size: 0.7rem !important; letter-spacing: 1.5px !important;">Reservar</a>
                    </div>
                </div>
                """)
            st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# SEÇÃO 3: LOJINHA / O CATÁLOGO
# ==========================================
elif secao == "lojinha":
    render_markdown("""
    <div class='fade-in' style='text-align: center; padding: 30px 0;'>
        <span class='editorial-subtitle'>Cuidado Profissional em Casa</span>
        <h1 class='editorial-title'>Catálogo de Produtos</h1>
        <div class='gold-divider'></div>
    </div>
    """)
    
    # Grid de Produtos (3 por linha para evitar achatamento e cortes)
    produtos = dados['produtos']
    cols_per_row = 3
    
    for i in range(0, len(produtos), cols_per_row):
        chunk = produtos[i:i+cols_per_row]
        cols_produtos = st.columns(cols_per_row)
        
        for idx, prod in enumerate(chunk):
            prod_img_b64 = carregar_imagem_base64(prod['imagem'])
            mime_type = "image/jpeg" if prod['imagem'].lower().endswith(('.jpg', '.jpeg')) else "image/png"
            
            with cols_produtos[idx]:
                msg_produto = dados['contato']['mensagem_produto'].format(produto=prod['nome'])
                link_compra = gerar_link_whatsapp(
                    dados['contato']['telefone_whatsapp'],
                    msg_produto
                )
                
                # Renderiza o card do produto inteiro em um único bloco HTML
                render_markdown(f"""
                <div class='luxury-card fade-in' style='text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 30px;'>
                    <div>
                        <div style="border: 1px solid rgba(230, 194, 128, 0.12); padding: 15px; background: rgba(12,11,10,0.5); margin-bottom: 20px; text-align: center; display: flex; align-items: center; justify-content: center; height: 320px;">
                            <img src="data:{mime_type};base64,{prod_img_b64}" style="max-height: 290px; max-width: 100%; object-fit: contain;">
                        </div>
                        <span style="font-family: 'Tenor Sans', sans-serif; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.95rem; color: #FAF7F2; display: block; margin-bottom: 8px; min-height: 48px; line-height: 1.4;">
                            {prod['nome']}
                        </span>
                        <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.05rem; color: #A09386; min-height: 80px; line-height: 1.5; margin-bottom: 15px; text-align: center;">
                            {prod['descricao']}
                        </p>
                        <div style="font-family: 'Cormorant Garamond', serif; font-size: 1.35rem; font-weight: 500; color: #E6C280; margin-bottom: 20px;">
                            R$ {prod['preco']:.2f}
                        </div>
                    </div>
                    <a href="{link_compra}" target="_blank" class="luxury-btn">Encomendar</a>
                </div>
                """)

# ==========================================
# SEÇÃO 4: CONTATO & LOCALIZAÇÃO
# ==========================================
elif secao == "contato":
    render_markdown("""
    <div class='fade-in' style='text-align: center; padding: 30px 0;'>
        <span class='editorial-subtitle'>Agende sua Experiência</span>
        <h1 class='editorial-title'>Localização & Contato</h1>
        <div class='gold-divider'></div>
    </div>
    """)
    
    col_info, col_mapa = st.columns([8, 12])
    
    with col_info:
        # Resolve horários de atendimento em HTML formatado inline
        horarios_html = "".join([f"<span style='color: #A09386; display: block; font-size: 0.85rem; margin-top: 4px;'>• {horario}</span>" for horario in dados['contato']['horarios']])
        
        # Renderiza a caixa de contato inteira em um único bloco HTML para garantir consistência
        render_markdown(f"""
        <div class='luxury-card fade-in' style='height: 100%; display: flex; flex-direction: column; justify-content: space-between;'>
            <div>
                <span style="font-family: 'Tenor Sans', sans-serif; text-transform: uppercase; letter-spacing: 2px; color: #C5A880; font-size: 0.75rem; display: block; margin-bottom: 10px;">Contato Direto</span>
                <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 300; margin: 0 0 20px 0; color: #FAF7F2;">Dinara Soares Beauty</h3>
                
                <p style="margin-bottom: 25px; line-height: 1.6; font-family: 'Tenor Sans', sans-serif; font-size: 0.9rem;">
                    <strong>Endereço:</strong><br>
                    <span style="color: #A09386; display: block; margin-top: 4px;">{dados['contato']['endereco']}</span>
                </p>
                
                <p style="margin-bottom: 25px; line-height: 1.6; font-family: 'Tenor Sans', sans-serif; font-size: 0.9rem;">
                    <strong>Funcionamento:</strong><br>
                    {horarios_html}
                </p>
                
                <p style="margin-bottom: 30px; line-height: 1.6; font-family: 'Tenor Sans', sans-serif; font-size: 0.9rem;">
                    <strong>Fale Conosco:</strong><br>
                    <span style="color: #E6C280; font-size: 1rem; font-weight: 500; display: block; margin-top: 4px;">WhatsApp: (38) 99161-7240</span>
                </p>
            </div>
            <a href="{link_geral_whatsapp}" target="_blank" class="luxury-btn">💬 Conversar no WhatsApp</a>
        </div>
        """)
        
    with col_mapa:
        st.markdown("<div class='fade-in' style='height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<p style='font-family: \"Tenor Sans\", sans-serif; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: #FAF7F2; margin-bottom: 15px;'>Visualizar no Mapa</p>", unsafe_allow_html=True)
        # Embutir o mapa via iframe do Google Maps configurado no JSON
        st.components.v1.html(
            f"""
            <iframe 
                src="{dados['contato']['link_maps']}" 
                width="100%" 
                height="370" 
                style="border:0; outline: none; box-shadow: 0 10px 40px rgba(0,0,0,0.5);" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
            """,
            height=390
        )
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# RODAPÉ DE ALTA MODA
# ==========================================
render_markdown(f"""
<div class='footer'>
    <p style='font-family: "Tenor Sans", sans-serif; text-transform: uppercase; letter-spacing: 3px; font-size: 0.8rem; margin-bottom: 5px; color: #FAF7F2;'>
        {dados['salao']['nome']}
    </p>
    <p style='font-family: "Cormorant Garamond", serif; font-style: italic; font-size: 1.05rem; color: #A09386;'>
        Sua beleza refletida na sua melhor versão. | Todos os direitos reservados © 2026.
    </p>
</div>
""")
