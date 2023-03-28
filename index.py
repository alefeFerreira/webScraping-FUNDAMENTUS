import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_completa = []
lista_Percorre = ["VALE3", "PETR4", "ITUB4", "BBDC4", "B3SA3", "MGLU3", "PETR3", "SUZB3", "CSNA3", "JBSS3", "USIM5", "GGBR4", "BBAS3", 
"RENT3", "RDOR3", "ITSA4", "VIIA3", "BPAC11", "ABEV3", "PRIO3", "WEGE3", "CASH3", "LREN3", "BRDT3", "BIDI11", "NTCO3", "GNDI3", "EMBR3", 
"AMER3", "CSAN3", "BRKM5", "ASAI3", "HAPV3", "RAIL3", "EQTL3", "BRAP4", "KLBN11", "CVCB3", "MRFG3", "ELET3", "AZUL4", "TOTS3", "CYRE3", 
"LAME4", "PETZ3", "CCRO3", "LWSA3", "UGPA3", "ALPA4", "RADL3", "MULT3", "BBSE3", "COGN3", "BRFS3", "BRML3", "GOAU4", "BBDC3", "CMIG4", 
"GOLL4", "SBSP3", "BIDI4", "BPAN4", "VIVT3", "HYPE3", "SULA11", "CPLE6", "AMBP3", "SANB11", "POSI3", "TAEE11", "ENEV3", "PSSA3", "LCAM3", 
"CIEL3", "QUAL3", "IRBR3", "RAIZ4", "CRFB3", "BEEF3", "FHER3", "MRVE3", "ELET6", "YDUQ3", "OIBR3", "SOMA3", "TIMS3", "ENGI11", "IGTA3", 
"VIVR3", "CPFE3", "INTB3", "PCAR3", "CMIN3", "DXCO3", "WIZS3", "ECOR3", "SLCE3", "EGIE3", "ARZZ3", "EZTC3", "RRRP3", "CESP6", "MOVI3", 
"ENBR3", "VAMO3", "ITUB3", "FLRY3", "SIMH3", "RAPT4", "TRPL4", "ETER3", "NEOE3", "VIVA3", "SAPR11", "LJQQ3", "SMTO3", "AMAR3", "SMFT3", 
"FESA4", "GMAT3", "TASA4", "STBP3", "LIGT3", "PTBL3", "OMGE3", "MDIA3", "ONCO3", "ANIM3", "GRND3", "SEQL3", "ALSO3", "ESPA3", "TEND3", 
"JHSF3", "LAME3", "CSMG3", "SBFG3", "ENAT3", "LEVE3", "SQIA3", "AERI3", "UNIP6", "BRPR3", "CEAB3", "CXSE3", "RCSL3", "MYPK3", "TUPY3", 
"CBAV3", "GGPS3", "BKBR3", "BMOB3", "DIRR3", "ALUP11", "BRSR6", "MLAS3", "HBSA3", "BIDI3", "AESB3", "MOSI3", "CLSA3", "TRAD3", "AALR3", 
"GFSA3", "IFCM3", "AGRO3", "SAPR4", "BRBI11", "ORVR3", "LOGN3", "ABCB4", "EVEN3", "PGMN3", "CPLE3", "CPLE11", "PNVL3", "ARML3", "TRIS3", 
"ENJU3", "ODPV3", "BLAU3", "CAML3", "LOGG3", "BOAS3", "ROMI3", "MEAL3", "POMO4", "ALLD3", "TECN3", "RANI3", "TTEN3", "LUPA3", "RECV3", 
"PARD3", "GUAR3", "DASA3", "BRAP3", "TPIS3", "SEER3", "NGRD3", "KEPL3", "MILS3", "TGMA3", "MATD3", "OPCT3", "LVTC3", "DEXP3", "MODL11", 
"USIM3", "CMIG3", "JPSA3", "LAVV3", "CURY3", "CARD3", "VVEO3", "DESK3", "HBOR3", "MTRE3", "AURA33", "POWE3", "BRIT3", "VULC3", "FIQE3", 
"JALL3", "MMXM3", "BMGB4", "JSLG3", "PMAM3", "TCSA3", "PLPL3", "AZEV4", "CSED3", "APER3", "SHUL4", "WEST3", "ELMD3", "SOJA3", "SYNE3", 
"SHOW3", "BBRK3", "KLBN4", "RCSL4", "VLID3", "CRPG5", "GPIV33", "LPSB3", "MELK3", "INEP4", "TFCO4", "VITT3", "DMMO3", "FRAS3", "INEP3", 
"UNIP3", "MDNE3", "SAPR3", "JFEN3", "GGBR3", "KRSA3", "TAEE4", "LLIS3", "NINJ3", "ITSA3", "PDGR3", "WSON33", "OIBR4", "G2DI33", "AGXY3", 
"PFRM3", "AZEV3", "MBLY3", "COCE5", "MOAR3", "EUCA4", "PDTC3", "TASA3", "LAND3", "KLBN3", "TAEE3", "DMVF3", "RSID3", "SANB4", "DOTZ3", 
"POMO3", "BRKM3", "PTNT3", "SGPS3", "PRNR3", "OFSA3", "RNEW4", "PINE4", "RSUL4", "CGRA4", "HBRE3", "SANB3", "TCNO4", "CGAS5", "IGBR3", 
"MODL4", "GOAU3", "RAPT3", "CLSC4", "RDNI3", "SLED4", "CAMB3", "RPMG3", "UCAS3", "PTNT4", "CEBR6", "CEBR3", "SULA4", "SCAR3", "EALT4", 
"ATMP3", "CEBR5", "RNEW3", "TCNO3", "MODL3", "HOOT4", "ATOM3", "SULA3", "CESP3", "DEXP4", "MNPR3", "EMAE4", "ALPA3", "ALPK3", "BPAC3", 
"MWET4", "HAGA4", "CRPG6", "RNEW11", "BIOM3", "SLED3", "WHRL4", "MTSA4", "AVLL3", "ENGI4", "ALUP4", "EEEL4", "BOBR4", "ENMT3", "BEES3", 
"MGEL4", "EUCA3", "ENGI3", "BPAC5", "TELB4", "WHRL3", "ALUP3", "MSPA3", "BRSR3", "CGRA3", "CEPE3", "CTNM4", "CTKA4", "CTSA4", "MNDL3", 
"TELB3", "CEGR3", "EQPA3", "EPAR3", "WLMM4", "OSXB3", "BMEB4", "FRTA3", "ENMT4", "EQPA7", "DOHL4", "SHUL3", "BALM4", "HAGA3", "LUXM4", 
"TRPL3", "CTSA3", "BMEB3", "CEEB3", "BAZA3", "EEEL3", "NORD3", "CEDO4", "BSLI3", "PATI3", "UNIP5", "PLAS3", "BAHI3", "ECPR4", "HETA3", 
"BAUH4", "MTIG4", "ODER4", "EKTR3", "TEKA4", "BMKS3", "HBTS5", "REDE3", "FESA3", "BEES4", "LIPR3", "GSHP3", "JOPA4", "PEAB3", "CBEE3", 
"SNSY5", "EKTR4", "EQPA5", "CGAS3", "BNBR3", "ESTR4", "NUTR3", "CSRN6", "SOND5", "BGIP4", "CEPE5", "CRPG3", "TXRX4", "CSRN3", "WLMM3", 
"CLSC3", "HETA4", "BMIN4", "JOPA3", "BDLL3", "CPLE5", "MERC4", "CTKA3", "SOND6", "CRIV4", "BSLI4", "SNSY3", "GEPA3", "DTCY3", "PATI4", 
"MAPT3", "GEPA4", "PEAB4", "CSRN5", "CEED3", "CESP5", "CSAB3", "AFLT3", "FRIO3", "AHEB3", "MERC3", "ELET5", "BRGE3", "BDLL4", "BRIV4", 
"BGIP3", "CALI4", "MTSA3", "TKNO4", "BALM3", "CEDO3", "MWET3", "EALT3", "ECPR3", "COCE3", "MAPT4", "RPAD3", "MRSA6B", "CRDE3", "BMIN3", 
"CSAB4", "PPLA11", "AHEB6", "BRSR5", "CRIV3", "TEKA3", "CEEB5", "CEED4", "BRKM6", "MRSA3B", "AHEB5", "BRGE8", "MRSA5B", "TXRX3", "RPAD5", 
"GPAR3", "BRIV3", "DOHL3", "SOND3", "CTNM3", "RPAD6", "BRGE12", "CEPE6", "USIM6", "BRGE11", "BRGE6", "FNCN3", "BRGE5", "SNSY6", "MSPA4", 
"ESTR3", "EQPA6", "CORR4", "CASN3"]

for codigo in lista_Percorre:
    print("Requisição de código: ",codigo)
    lista_dados = []

    if codigo=="":
        continue

    agent = {"User-Agent":"Mozilla/5.0"}
    url = f"https://fundamentus.com.br/detalhes.php?papel={codigo}"
    
    response = requests.get(url, headers=agent)
    content = response.content
    
    site = BeautifulSoup(content, 'html.parser')
    dadosGeral = site.findAll('table', attrs={'class': 'w728'})
    
    for dado in dadosGeral:
        dadoBruto = dado.text 
        dadoFormatado = dadoBruto.replace("?", " ")
        lista_dados.append(dadoFormatado)


    transforma_string = ' '.join(lista_dados)
    Lista_detalhe = transforma_string.split("\n")   
    
    if len(Lista_detalhe) == 197:
        print("***************")
        print(f"-----> {len(Lista_detalhe)}")
        print(Lista_detalhe)
        print("***************") 
        papel = Lista_detalhe[3]
        cotacao = Lista_detalhe[5]
        tipo = Lista_detalhe[9]
        dataUltCot = Lista_detalhe[11] 
        empresa = Lista_detalhe[15]
        min_52_sem = Lista_detalhe[17]
        setor = Lista_detalhe[21]
        max_52_sem = Lista_detalhe[23]
        subsetor = Lista_detalhe[27]
        vol_med = Lista_detalhe[29]
        valor_mercado = Lista_detalhe[34]
        ult_balanco_processado = Lista_detalhe[36]
        valor_firma = Lista_detalhe[40]
        nro_acoes = Lista_detalhe[42]
        dia = Lista_detalhe[52]
        pl = Lista_detalhe[54]
        lpa = Lista_detalhe[56]
        mes = Lista_detalhe[60]
        pvp = Lista_detalhe[62]
        vpa = Lista_detalhe[64]
        trinta_dias = Lista_detalhe[68]
        p_ebit = Lista_detalhe[71]
        marg_bruta = Lista_detalhe[74]
        doze_meses = Lista_detalhe[78]
        psr = Lista_detalhe[81]
        marg_ebit = Lista_detalhe[84]
        dois_mil_vinte_um = Lista_detalhe[88]
        p_ativos = Lista_detalhe[91]
        marg_liquida = Lista_detalhe[94]
        dois_mil_vinte = Lista_detalhe[98] 
        p_cap_giro = Lista_detalhe[101]
        ebit_ativo = Lista_detalhe[103]
        dois_mil_dezenove = Lista_detalhe[107]
        p_ativo_circ_liq = Lista_detalhe[110]
        roic = Lista_detalhe[113]
        dois_mil_dezoito = Lista_detalhe[117]
        div_yield = Lista_detalhe[119]
        roe = Lista_detalhe[122]
        dois_mil_dezessete = Lista_detalhe[126]
        ev_ebitda = Lista_detalhe[129]
        liquidez_corr = Lista_detalhe[132]
        dois_mil_dezesseis = Lista_detalhe[136]
        ev_ebit = Lista_detalhe[139]
        div_patrim = Lista_detalhe[142]
        cresc_rec = Lista_detalhe[149]
        giro_ativos = Lista_detalhe[152]
        ativo = Lista_detalhe[160]
        depositos = Lista_detalhe[162]
        cart_de_credito = Lista_detalhe[166]
        patrim_liq = Lista_detalhe[168]
        result_int_financ_12_meses = Lista_detalhe[180]
        result_int_financ_3_meses = Lista_detalhe[182]
        rec_servicos_12_meses = Lista_detalhe[186]
        rec_servicos_3_meses = Lista_detalhe[188]
        lucro_liquido_12_meses = Lista_detalhe[192]
        lucro_liquido_3_meses = Lista_detalhe[194]

        lista_completa.append([papel,cotacao,tipo,dataUltCot,empresa,min_52_sem,setor,max_52_sem,subsetor,vol_med,
        valor_mercado,ult_balanco_processado,valor_firma,nro_acoes,dia,pl,lpa,mes,pvp,vpa,trinta_dias,p_ebit,marg_bruta,doze_meses,psr,
        marg_ebit,dois_mil_vinte_um,p_ativos,marg_liquida,dois_mil_vinte,p_cap_giro,p_ativo_circ_liq,ebit_ativo,dois_mil_dezenove,roic,
        dois_mil_dezoito,div_yield,roe,dois_mil_dezessete,ev_ebitda,liquidez_corr,dois_mil_dezesseis,ev_ebit,div_patrim,cresc_rec,
        giro_ativos,ativo,depositos,cart_de_credito,patrim_liq,result_int_financ_12_meses,result_int_financ_3_meses,
        rec_servicos_12_meses,rec_servicos_3_meses,lucro_liquido_12_meses,lucro_liquido_3_meses]) 

        
        excel = pd.DataFrame(lista_completa,columns=['Papel','Cotação','Tipo','Data última cotação','Empresa','Min 52 sem','Setor','Max_52_sem',
        'Subsetor','Volume médio','Valor de mercado','Último balanço processado','Valor de firma','N° ações','Dia','Pl','Lpa','Mês','Pvp','Vpa',
        '30 Dias','P/Ebit','Margem bruta','12 Meses','Psr','Margem/Ebit','2021','P/Ativos','Margem liquida','2020','P/Cap/Giro','P/Ativo/Circ/liq',
        'Ebit/Ativo','2019','Roic','2018','Div/Yeld','Roe','2017','Ev/Ebitda','Liquidez_Corr','2016','Ev/Ebit','Div/Patrim','Cresc/Rec','Giros ativos',
        'Ativo','Depósitos,','cartão de crédito','patrimônio liquido','resultado int 12 meses','resultado int 3 meses',
        'rec serviços 12 meses','rec serviços 3 meses','lucro liquido 3 meses','lucro liquido 12 meses'])
    else:  
        continue  


excel.to_excel('Fundamentus.xlsx', index=False)   
print("Completado com sucesso !")





