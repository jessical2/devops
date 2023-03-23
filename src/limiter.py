from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Define limiter, this makes it available across all routes
limiter = Limiter(
        get_remote_address,
        default_limits=["200 per day", "50 per hour"],
        )


