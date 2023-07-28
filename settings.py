from os import environ

SESSION_CONFIGS = [
       dict(
        name='Day1',
          display_name="Day1",
           num_demo_participants=2,   
            app_sequence=['pradelli_trust_game','pradelli_bret']),
           
       dict(
        name='pradelli_Day2',
          display_name="pradelli_Day2",
           num_demo_participants=2,
            app_sequence=['pradelli_Day2'],  
           )]

      # dict(
      #   name='Experiment_survey',
      #   display_name="Experiment_survey",
      #     num_demo_participants=4,
      #      app_sequence=['Experiment_survey']
      #     )
    # dict(
    # name='Pradelli_Project',
    #  display_name="Pradelli_Project",
    #   num_demo_participants=2,
    #  app_sequence=['Pradelli_Project']
     #)]
    #  dict(
    #   name='groups_roles',
    #    display_name="groups_roles",
    #     num_demo_participants=4,
    #     app_sequence=['groups_roles']
    #  )]
     


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5988942570582'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
