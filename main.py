import streamlit as st
from streamlit_option_menu import option_menu

# Import the resources dynamically based on selected menu
from Resources import home, free_api, chrome_extensions, frontend_tools, icons_website, python, react, django, vscode_extensions, web_scraping, style

# Set Streamlit layout to wide mode
st.set_page_config(page_title="UpBizz Tools", page_icon=":zap:", layout="wide")

# Define a dictionary to map menu items to their corresponding modules
PAGE_MODULES = {
    "Home": home,
    "Free API": free_api,
    "Chrome Extensions": chrome_extensions,
    "FrontEnd Tools": frontend_tools,
    "Icons Website": icons_website,
    "Python": python,
    "React": react,
    "Django": django,
    "VSCode Extensions": vscode_extensions,
    "Web Scraping": web_scraping
}

# 1. Sidebar menu with all the required items
with st.sidebar:
    selected = option_menu(
        "UpBizz Tools",
        list(PAGE_MODULES.keys()),  # Dynamically use the keys of the PAGE_MODULES dict
        icons=[
            "house", "cloud", "puzzle", "tools", "palette", "terminal", 
            "code-slash", "server", "link", "plug", "search", "gear"
        ],
        menu_icon="cast",
        default_index=0
    )

# Helper function to display tools (used for Free API, Chrome Extensions, etc.)
def display_tools(page_module, tools_list, custom_css):
    # Inject custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Filter tools based on the search term
    filtered_tools = [
        tool for tool in tools_list
        if search_term.lower() in tool['name'].lower() or search_term.lower() in tool['description'].lower()
    ]

    # Use Streamlit columns with adjusted ratios
    columns = st.columns([1, 1, 1])  # Three equal-width columns
    for idx, tool in enumerate(filtered_tools):
        col = columns[idx % 3]  # Cycle through columns
        with col:
            st.markdown(f"""
                <div class="card">
                    <img src="{tool['logo_url']}" alt="{tool['name']} logo">
                    <div class="card-title">{tool['name']}</div>
                    <div class="card-description">{tool['description']}</div>
                    <div class="card-footer">
                        <a href="{tool['store_link']}" target="_blank">
                            <button class="card-button">{tool['button_name']}</button>
                        </a>
                    </div>
                </div>
            """, unsafe_allow_html=True)


# Display content based on the selected menu item
if selected in PAGE_MODULES:
    page = PAGE_MODULES[selected]
    st.title(page.title)
    st.markdown(page.content)
    st.divider()

    if selected != "Home":
        # Global search input outside of specific page logic
        search_term = st.text_input("Search:", "")

    # Call the display_tools function for the selected page
    if selected == "Free API":
        display_tools(free_api, free_api.FREE_API_TOOLS, style.STYLE_CSS)
    elif selected == "Chrome Extensions":
        display_tools(chrome_extensions, chrome_extensions.CHROME_EXTENSIONS, style.STYLE_CSS)
    elif selected == "FrontEnd Tools":
        display_tools(frontend_tools, frontend_tools.FRONTEND_TOOLS, style.STYLE_CSS)
    elif selected == "Python":
        display_tools(python, python.PYTHON_TOOLS, style.STYLE_CSS)
    elif selected == "Icons Website":
        display_tools(icons_website, icons_website.ICONS_WEBSITE_TOOLS, style.STYLE_CSS)
    elif selected == "React":
        display_tools(react, react.REACT_TOOLS, style.STYLE_CSS)
    elif selected == 'Django':
        display_tools(django, django.DJANGO_TOOLS, style.STYLE_CSS)
    elif selected == 'VSCode Extensions':
        display_tools(vscode_extensions, vscode_extensions.VSCODE_EXTENSIONS, style.STYLE_CSS)
    elif selected == 'Web Scraping':
        display_tools(web_scraping, web_scraping.WEB_SCRAPING, style.STYLE_CSS)