# Models Documentation

## User Model
Represents a user in the system.

### Fields:
- `id`: Primary key, auto-incremented.
- `username`: Unique username.
- `email`: User email address.
- `date_joined`: Date when the user joined.

## Product Model
Represents a product available for orders.

### Fields:
- `id`: Primary key, auto-incremented.
- `name`: Name of the product.
- `price`: Price of the product.

## Order Model
Represents an order made by a user.

### Fields:
- `id`: Primary key, auto-incremented.
- `user`: ForeignKey to `User`, representing the owner of the order.
- `created_at`: Date and time when the order was created.

## OrderItem Model
Represents an item within an order.

### Fields:
- `id`: Primary key, auto-incremented.
- `order`: ForeignKey to `Order`, linking the item to a specific order.
- `product`: ForeignKey to `Product`, indicating which product was ordered.
- `quantity`: The number of products in the order item.
