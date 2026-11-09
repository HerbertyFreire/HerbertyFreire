<p align="center">
  <img src="./assets/header.svg" alt="Herberty Freire, Full Stack Developer · Ciência da Computação @ UFAL" width="100%"/>
</p>

<p align="center">
  <a href="mailto:herbertylive@gmail.com"><img src="https://img.shields.io/badge/email-herbertylive%40gmail.com-0b2a3a?style=for-the-badge&logo=gmail&logoColor=5eead4&labelColor=05121f" alt="Email"/></a>
  <img src="https://img.shields.io/badge/Maceió-Alagoas%2C%20BR-0b2a3a?style=for-the-badge&logo=googlemaps&logoColor=5eead4&labelColor=05121f" alt="Maceió, AL"/>
  <img src="https://komarev.com/ghpvc/?username=HerbertyFreire&style=for-the-badge&color=0d9488&label=visitas" alt="Visitas ao perfil"/>
</p>

---

### `> sobre`

Sou **desenvolvedor Full Stack** na **SEADES/AL** (Secretaria de Estado da Assistência e Desenvolvimento Social de Alagoas) e estudante de **Ciência da Computação no IC/UFAL**. Meu trabalho mora no encontro entre **software e política pública**: do **Observatório Socioassistencial de Alagoas** (VSA-AL), sistema que gerencio e desenvolvo de ponta a ponta, a painéis, relatórios e análises que transformam planilha bagunçada em decisão de gestão, de dados eleitorais por zona e local de votação a indicadores de comunidades quilombolas e do SUAS. Sempre com dados pessoais protegidos: o que é público sai anonimizado e agregado.

Na faculdade, pesquiso **redes**: meu TCC mede como a **comutação Cut-Through e Store-and-Forward** afetam a qualidade de experiência do **WebRTC** sob estresse, com simulações no **ns-3**. Agora estou me aprofundando em **engenharia de IA** (LLMs, RAG, agentes e MCP) e colocando em prática na **Eleven**, meu segundo cérebro.

```ts
const herberty = {
  agora:       ["Full Stack Jr. @ SEADES/AL", "Ciência da Computação @ UFAL"],
  antes:       ["Gerente de projeto & full stack @ Imersão Brisa", "Estágio dev @ SEADES/AL", "Estágio @ SECULT/AL"],
  pesquisa:    "QoE de WebRTC sob estresse de rede (ns-3)",
  estudando:   "engenharia de IA: LLMs, RAG, agentes e MCP",
  construindo: ["Observatório VSA-AL", "Eleven", "RiderSync", "Aboio"],
  idiomas:     ["pt-BR", "en", "es"],
  lema:        "resolver com o que já existe antes de adicionar mais uma dependência",
};
```

### `> stack`

<p align="center">
  <img src="https://skillicons.dev/icons?i=c,cpp,py,java,js,ts,nodejs,html,css&perline=9" alt="Linguagens"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=react,vite,tailwind,express,fastapi,postgres,supabase,prisma,sequelize&perline=9" alt="Frameworks e bancos"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=django,laravel,latex,git,github,githubactions,vercel,linux,vscode&perline=9" alt="Ferramentas"/>
</p>

<p align="center">
  <sub>também: <b>ns-3</b> · <b>Capacitor</b> · <b>DuckDB</b> · <b>Power BI</b> · <b>Stripe</b> · <b>WebSockets</b> · <b>JWT</b> · <b>OpenGL</b> · <b>Render</b> · análise de dados públicos e visualização</sub>
</p>

### `> pesquisa`

<p align="center">
  <img src="./assets/tcc.svg" alt="TCC: 630 execuções no ns-3; latência Store-and-Forward de 0,14–0,38 ms no regime controlado, 2,0–2,6 ms congestionado e 3,5–3,7 ms na saturação; Cut-Through reduz até 15,8% sem carga e menos de 1% sob congestionamento" width="100%"/>
</p>

<sub>630 execuções de 300 s (9 combinações de codecs de voz e vídeo × 7 cargas de 30 a 200 Mbps × 10 sementes), com o Cut-Through estimado por um modelo contrafactual por pacote. Três regimes aparecem: controlado, congestionado e saturação. O Cut-Through corta até 15,8% da latência do vídeo com a rede folgada, mas o ganho cai para menos de 1% sob carga, porque a maioria dos pacotes encontra a porta ocupada. Conclusão: num salto, o atraso de fila supera em uma ordem de grandeza o efeito do método de comutação e dos codecs. IC 95% de no máximo 5,3% da média; MOS de voz entre 4,10 e 4,41. Orientação: Prof. Dr. Almir Pereira Guimarães.</sub>

### `> projetos em destaque`

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🏛️ Observatório Socioassistencial de Alagoas <sup><code>SEADES/AL</code></sup></h4>
      Portal de indicadores do SUAS com três áreas: observatório público (só dados agregados), área técnica restrita para a vigilância socioassistencial e módulo de calamidades. Pipeline Python/DuckDB remove dados pessoais antes de gerar indicadores. Gerência do projeto e full stack.
      <br/><br/>
      <img src="https://img.shields.io/badge/React-0b2a3a?style=flat-square&logo=react"/>
      <img src="https://img.shields.io/badge/Node.js-0b2a3a?style=flat-square&logo=nodedotjs"/>
      <img src="https://img.shields.io/badge/PostgreSQL-0b2a3a?style=flat-square&logo=postgresql"/>
      <img src="https://img.shields.io/badge/DuckDB-0b2a3a?style=flat-square&logo=duckdb"/>
    </td>
    <td width="50%" valign="top">
      <h4>🐄 Aboio <sup><code>pausado · rumo a SaaS</code></sup></h4>
      Gestão de fazendas (rebanho, plantio, leite e finanças) num só código para web, Android e iPhone. Offline-first com fila de sincronização, Row Level Security em todas as tabelas, assinaturas via Stripe e 155 testes de invasão rodando no CI.
      <br/><br/>
      <img src="https://img.shields.io/badge/React-0b2a3a?style=flat-square&logo=react"/>
      <img src="https://img.shields.io/badge/Supabase-0b2a3a?style=flat-square&logo=supabase"/>
      <img src="https://img.shields.io/badge/Capacitor-0b2a3a?style=flat-square&logo=capacitor"/>
      <img src="https://img.shields.io/badge/Stripe-0b2a3a?style=flat-square&logo=stripe"/>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🧠 Eleven <sup><code>em construção</code></sup></h4>
      Meu segundo cérebro: notas em Markdown ligadas entre si, lidas por todas as minhas IAs, com sincronização automática pelo Git, visualizador em forma de cérebro e um servidor MCP em projeto (com busca semântica na fase seguinte).
      <br/><br/>
      <img src="https://img.shields.io/badge/MCP-0b2a3a?style=flat-square"/>
      <img src="https://img.shields.io/badge/LLMs-0b2a3a?style=flat-square"/>
      <img src="https://img.shields.io/badge/Obsidian-0b2a3a?style=flat-square&logo=obsidian"/>
    </td>
    <td width="50%" valign="top">
      <h4>🗳️ <a href="https://github.com/HerbertyFreire/alagoas-2turno">Raio-X eleitoral de Alagoas</a></h4>
      Análise interativa das eleições de 2026 em Alagoas por município, zona, local de votação e faixa etária, apresentada à gestão estadual e publicada na Vercel.
      <br/><br/>
      <img src="https://img.shields.io/badge/HTML-0b2a3a?style=flat-square&logo=html5&logoColor=fb923c"/>
      <img src="https://img.shields.io/badge/dados%20públicos-0b2a3a?style=flat-square"/>
      <img src="https://img.shields.io/badge/Vercel-0b2a3a?style=flat-square&logo=vercel"/>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🆘 Sistema de Calamidades SUAS <sup><code>SEADES/AL</code></sup></h4>
      Consulta ao Cadastro Único para localizar e atender famílias em zonas de risco durante calamidades, com registro de ocorrências e indicadores de vulnerabilidade. Virou um artigo e evoluiu para o módulo de calamidades do Observatório.
      <br/><br/>
      <img src="https://img.shields.io/badge/Python-0b2a3a?style=flat-square&logo=python"/>
      <img src="https://img.shields.io/badge/FastAPI-0b2a3a?style=flat-square&logo=fastapi"/>
      <img src="https://img.shields.io/badge/SQLite-0b2a3a?style=flat-square&logo=sqlite"/>
    </td>
    <td width="50%" valign="top">
      <h4>🗺️ Caso Braskem <sup><code>SEADES/AL</code></sup></h4>
      Estudo sobre para onde foram os moradores dos bairros de Maceió afetados pelo afundamento do solo e a pressão que isso gerou nos CRAS e CREAS, com mapa interativo de fluxos de deslocamento. Tudo compartilhado de forma anonimizada e agregada por bairro.
      <br/><br/>
      <img src="https://img.shields.io/badge/Python-0b2a3a?style=flat-square&logo=python"/>
      <img src="https://img.shields.io/badge/mapas-0b2a3a?style=flat-square"/>
      <img src="https://img.shields.io/badge/Power%20BI-0b2a3a?style=flat-square&logo=powerbi"/>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>📍 <a href="https://github.com/HerbertyFreire/SpotLy">SpotLy</a></h4>
      Back-end em Node.js com autenticação JWT, ORM Prisma, processamento de imagens com Sharp e recuperação de senha por e-mail, em produção no Render.
      <br/><br/>
      <img src="https://img.shields.io/badge/Node.js-0b2a3a?style=flat-square&logo=nodedotjs"/>
      <img src="https://img.shields.io/badge/Prisma-0b2a3a?style=flat-square&logo=prisma"/>
      <img src="https://img.shields.io/badge/JWT-0b2a3a?style=flat-square&logo=jsonwebtokens"/>
    </td>
    <td width="50%" valign="top">
      <h4>🎸 RiderSync</h4>
      Plataforma para artistas independentes de Alagoas: gestão de rider técnico/backline entre bandas e casas de show, currículo da banda e monitoramento de editais de fomento cultural.
      <br/><br/>
      <img src="https://img.shields.io/badge/Projetão%20UFAL-0b2a3a?style=flat-square"/>
      <img src="https://img.shields.io/badge/economia%20criativa-0b2a3a?style=flat-square"/>
    </td>
  </tr>
</table>

<sub>📊 Também na SEADES/AL: painel de Educação Permanente do SUAS, relatórios do CEAS/AL com o Censo SUAS e mapas de comunidades quilombolas. Sistemas internos não têm repositório público.</sub>

<details>
<summary><b>Mais coisas por aqui</b></summary>
<br/>

| Projeto | O que é |
|---|---|
| [RecalIC](https://github.com/HerbertyFreire/RecalIC) | Sistema de gestão de ocorrências do Instituto de Computação da UFAL (Laravel) |
| QuemFaz <sup>pausado</sup> | Marketplace de serviços domésticos: app do cliente, do prestador e painel admin, com máquina de estados do chamado no servidor |
| [Conversor-MPEG-para-MP4](https://github.com/HerbertyFreire/Conversor-MPEG-para-MP4) | Conversão de vídeos em lote, local, nascida de um problema real no trabalho (Python) |
| [MyFood](https://github.com/HerbertyFreire/MyFood) | Projeto da disciplina de Programação 2 (Java) |
| [Chatbot-clinica-Odontologica](https://github.com/HerbertyFreire/Chatbot-clinica-Odontologica) | Chatbot de atendimento para clínica odontológica (JavaScript) |
| [Diagnostico-de-veterinario](https://github.com/HerbertyFreire/Diagnostico-de-veterinario) | Sistema de consulta e diagnóstico veterinário com *frames* (disciplina de IA) |
| [GraphAlgorithms-](https://github.com/HerbertyFreire/GraphAlgorithms-) | Algoritmos em grafos em C++ |
| [Planetas-Orbitando-](https://github.com/HerbertyFreire/Planetas-Orbitando-) · [Campo-de-Futebol](https://github.com/HerbertyFreire/Campo-de-Futebol) | Computação gráfica com OpenGL |
| [Centro-Historico](https://github.com/HerbertyFreire/Centro-Historico) | Projeto em Python |
| Chat WebSocket | Servidor de chat com broadcast e sessões (`ws`), da disciplina de Sistemas Distribuídos |

</details>

### `> números`

<p align="center">
  <img src="https://raw.githubusercontent.com/HerbertyFreire/HerbertyFreire/output/stats.svg" alt="Estatísticas e linguagens mais usadas no GitHub" width="100%"/>
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=HerbertyFreire&hide_border=true&background=05121f&ring=5eead4&fire=fbbf24&currStreakLabel=5eead4&sideLabels=cbd5e1&currStreakNum=f8fafc&sideNums=f8fafc&dates=94a3b8&stroke=0b2a3a&locale=pt_BR" alt="Sequência de contribuições"/>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/HerbertyFreire/HerbertyFreire/output/snake-dark.svg"/>
    <img src="https://raw.githubusercontent.com/HerbertyFreire/HerbertyFreire/output/snake.svg" alt="Cobrinha comendo o gráfico de contribuições"/>
  </picture>
</p>

<p align="center">
  <img src="./assets/footer.svg" alt="Feito em Maceió, Alagoas" width="100%"/>
</p>
