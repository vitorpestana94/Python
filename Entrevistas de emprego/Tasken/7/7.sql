SELECT x.nome, COUNT(y.cpf_cliente) AS quantidade
FROM Clientes x
JOIN Telefones y ON x.cpf = y.cpf_cliente
GROUP BY x.nome
HAVING COUNT(y.cpf_cliente) >= 1;