Используем DISTINCT, т.к. номера заказов задваиваютсч в  БД из-за бага в приложении

SELECT cr.login, 
			COUNT(DISTINCT ord.track)
FROM "Couriers" AS cr
LEFT OUTER JOIN "Orders" AS ord ON cr.id=ord."courierId"
WHERE ord."inDelivery"=True
GROUP BY cr.login


В этом запросе я не использую DISTINCT, т.к. у дублей заказов могут быть разные статусы

SELECT track, 
			CASE 
				WHEN finished=True THEN 2
				WHEN canсelled=True THEN -1
				WHEN "inDelivery" =True THEN 1
				ELSE 0
			END
FROM "Orders"
