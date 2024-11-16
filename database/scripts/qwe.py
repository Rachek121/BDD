import pytest
from db import temp_db, Data

@pytest.fixture(scope="function")
def data(temp_db):
    return Data(temp_db)

@pytest.mark.parametrize("orders", [
    [{"type_of_work": "Repair", "description": "Fix broken screen", "acceptance_date": "2022-01-01", "customer": "John Doe", "executor": "Jane Smith", "status": "In progress"}],
    [{"type_of_work": "Repair", "description": "Fix broken screen", "acceptance_date": "2022-01-01", "customer": "John Doe", "executor": "Jane Smith", "status": "In progress"},
     {"type_of_work": "Installation", "description": "Install new software", "acceptance_date": "2022-01-02", "customer": "Bob Johnson", "executor": "Alice Brown", "status": "Completed"}],
])
def test_add_orders(data, orders):
    for order in orders:
        result = data.add_order(**order)
        assert result == "Запись добавлена"
        print(f"Added order: {order}")

    all_orders = data.get_all_orders()
    print(f"Retrieved orders: {all_orders}")
    assert len(all_orders) == len(orders)
    for i, order in enumerate(orders):
        assert all_orders[i][1:] == tuple(order.values())