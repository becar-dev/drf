from drf_yasg.generators import OpenAPISchemaGenerator

class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self, *args, **kwargs):
        return {
            'Basic': {
                'type': 'basic',
                'description': 'Basic auth (username/password)'
            },
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'JWT authorization header. Format: Bearer <your_token>'
            },
            'Token': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'DRF token header. Format: Token <your_token>'
            }
        }
