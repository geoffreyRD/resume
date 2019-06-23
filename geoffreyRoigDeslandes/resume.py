# !/usr/bin/env python3
class Resume:
    """
    Hello,

    Thank you for taking the time to review my application :)

    The first part of the document defines all the functions I need to enter all
    the relevent information about my application. If you are not interested in
    this technical part, you can jump directly to line 92.

    I hope you will enjoy reading it as I had a good time writing it :)

    Thanks again,

    Geoffrey
    """
    def __init__(
            self,
            first_name: str,
            last_name: str,
            address: dict,
            email: str,
            phone_number: int,
            LinkedIn: str,
            nationality: str,
            spoken_languages: list):
        """
        In this __init__ function you can find my personal information.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.LinkedIn = LinkedIn
        self.nationality = nationality
        self.spoken_languages = spoken_languages

    @staticmethod
    def education(
            degree: str,
            major: str,
            university: str,
            country: str,
            from_: str,
            to_: str,
            main_classes: list):

        list_course = ', '.join(map(str, main_classes))

        output = f""" I have a {degree} from {university}.
        I studied there from {from_} to {to_}.
        During my scholarship here I studied {list_course}.
        """
        return output

    @staticmethod
    def experience(
            company: str,
            position: str,
            city: str,
            country: str,
            from_: str,
            to_: str,
            achievements: list):

        list_task = ', '.join(map(str, achievements))

        if to_ == 'Current':
            output = f"""I currently work as a {position} at {company}.
            I have been working there since {to_}, amongst other tasks, I {list_task}.
            """
        else:
            output = f"""I worked as a {position} at {company} between {from_} and {to_}.
            Amongst other tasks, I {list_task}.
            """
        return output

        @staticmethod
        def activities(
                association: str,
                role: str,
                city: str,
                country: str,
                from_: str,
                to_: str,
                description: str):
            return descripion


####################################################################################################
# PROFILE

Geoffrey_Roig_Deslandes = Resume(
    first_name='Geoffrey',
    last_name='Roig-Deslandes',
    address={
        'Street': 'Saint Charles',
        'Number': '2855A'
        'Appartement Number': '102',
        'Zip Code': 'H3K 3J1',
        'City': 'Montreal',
        'Contry': 'Canada'
    },
    email='geoffrey.roig@gmail.com',
    phone_number='+1 514 582 3431',
    LinkedIn='https://www.linkedin.com/in/geoffreyroig/?locale=en_US',
    nationality='French',
    spoken_languages={
        'Danish': 'In Progress :)'
        'English': 'Fluent',
        'French': 'Fluent',
        'German': 'Basics'})

####################################################################################################
# PROFESSIONAL EXPERIENCE

data_analyst = read.experience(
    company='Behaviour Interactive',
    position='Data Analyst',
    city='Montreal',
    country='Canada',
    from_='November 2017',
    to_='Current',
    achievements=[
        'Developed a player segmentation analysis using K-Means method',
        'Created a model to identify potential whales based on a decision tree model',
        'Trained 3 interns, one of them was hired after his internship',
        'Developed and maintained dashboard and reports using PowerBI',
        'Developed on server-to-server script for data management purposes'
    ])

bi_analyst = read.experience(
    company='Keolis Canada',
    position='Business Intelligence Analyst',
    city='Montreal',
    country='Canada',
    from_='Juin 2016',
    to_='November 2017',
    achievements=[
        'Developed a neural network model to estimate churn risk of customers',
        'Created and maintained a predictive model for sales, using Holt & Winters method',
        'Produced ad hoc analysis for marketing campaigns',
        'Created and maintained dashboards  and reports to the attention of upper management',
        'Initiated a knowledge sharing initiative (Lunch & Learn)'
    ])

internship = read.experience(
    company='Gameloft',
    position='Data Science Intern',
    city='Montreal',
    country='Canada',
    from_='May 2015',
    to_='August 2015',
    achievements=[
        'Redacted a literature review on neural networks',
        'Referenced and organized data analytics scripts to standardize the production of analyses',
        'Produced cases of study to improve documentation and support business performance managers'
    ])

analyst = read.experience(
    company='Interface Transport',
    position='Transportation Analyst',
    city='Lyon',
    country='France',
    from_='February 2012',
    to_='July 2012',
    achievements=[
        'Redacted a report on the compatibility of public and private transit for urban freight'
    ])

####################################################################################################
# EDUCATION
msc_marketing = read.education(
    degree='Master of Science',
    major='Marketing',
    university='HEC Montreal',
    country='Canada',
    from_='January 2014',
    to_='March 2016',
    main_classes=[
        'Data Mining', 'Text Mining',
        'Multidimentional Data Analysis',
        'Quantitative Matketing',
        'Product and Innovation Management',
        'Customer Behaviour', 'Demand Analysis'
    ])

m2_economics = read.education(
    degree='Master 2',
    major='Economics',
    university='Universite de Montpellier 1',
    country='France',
    from_='September 2009',
    to_='October 2011',
    main_classes=[
        'Econometrics', 'Data Analysis',
        'Forecasting Methods', 'Game Theory'
    ])

bachelor_economics = read.education(
    degree='Master 2',
    major='Economics',
    university='Universite de Montpellier 1',
    country='France',
    from_='September 2009',
    to_='October 2011',
    main_classes=[
        'Microeconomics', 'Statistics',
        'Macroeconomics', 'Finance'
    ])

####################################################################################################
# ACTIVITIES
water_polo_referee = read.activities(
    association='Waterpolo Quebec',
    role='Referee',
    city='Montreal',
    country='Canada',
    from_='October 2013',
    to_='Current',
    description="""
    Being a referee taught me to be relentless and to
    learn from my mistakes. It has been one of the greatest challenge I ever met,
    and I proud to say that it helped me be a better person.
    """)

water_polo_player = read.activities(
    association='ACC Waterpolo',
    role='Player',
    city='Montreal',
    country='Canada',
    from_='February 2013',
    to_='September 2018',
    description="""
    Playing waterpolo helped me develop
    my team spirit and leadership as I also coached the team.
    """)

Ludos = read.activities(
    association='Ludos HEC',
    role='Member and Vice-President',
    city='Montreal',
    country='Canada',
    from_='September 2014',
    to_='December 2015',
    description="""
    Ludos is a student association whom goal is
    to promote the videogame industry to HEC students.
    """)
