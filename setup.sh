mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"jeevisiran21@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
hardless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml