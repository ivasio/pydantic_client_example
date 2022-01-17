echo "Client started. Waiting for servers to start"
sleep 10

echo "Get current orders"
httpx -m GET 'http://personal_page_server:8080/orders'

echo "Add new order"
sleep 1
httpx -m PUT 'http://personal_page_server:8080/orders' --json '{"price": 20, "pet_category":"cat", "order": {}}'

echo "Get updated orders"
sleep 1
httpx -m GET 'http://personal_page_server:8080/orders'
