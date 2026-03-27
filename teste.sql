select 
    Coluna_cardapio
from 
    tabela_pizzaria
where 
    data_do_cardapio = '2024-06-01';



select 
    Coluna_cardapio
from 
    tabela_pizzaria
    left join tabela_bebidas
    on tabela_pizzaria.id = tabela_bebidas
where 
    data_do_cardapio = '2024-06-01';


--CTEs
with Cardapio as (
    select 
        Coluna_cardapio
    from 
        tabela_pizzaria
    where 
        data_do_cardapio = '2024-06-01'
),
Bebidas as (
    select 
        Coluna_bebida
    from 
        tabela_bebidas
    where 
        data_do_cardapio = '2024-06-01'
)
select 
    Cardapio.Coluna_cardapio,
    Bebidas.Coluna_bebida 
    from Cardapio
    left join Bebidas
    on Cardapio.id = Bebidas.id;


--CAST
select 
    coluna_numero_pedido -- supondo que seja do tipo inteiro
    coluna_nome_pedido -- supondo que seja do tipo texto
    CASE
        when coluna_numero_pedido = coluna_nome_pedido then "resultado - vai dar erro porque são tipos diferentes"
        else "foda"
    end as comparacao

select 
    cast(coluna_numero_pedido as text) -- supondo que seja do tipo inteiro
    coluna_nome_pedido -- supondo que seja do tipo texto
    CASE
        when coluna_numero_pedido = coluna_nome_pedido then "resultado - vai dar certo porque são tipos certos"
        else "foda"
    end as comparacao
