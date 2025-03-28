# Views Documentation

## API Views

### UserViewSet
Handles CRUD operations for `User`.

### ProductViewSet
Handles CRUD operations for `Product`.

### OrderViewSet
Handles CRUD operations for `Order`.

### OrderItemViewSet
Handles CRUD operations for `OrderItem`.

### API Home (`api_home`)
Returns a list of all available API routes.

## Utility Functions

### collect_routes(patterns, request, prefix="")
Recursively collects all API routes and filters invalid ones.

### get_base_url(request=None)
Returns the base URL based on the environment (local server or GitHub Codespaces).