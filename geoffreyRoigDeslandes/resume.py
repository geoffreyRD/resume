# !/usr/bin/env python3
class Resume:
    """
    Hello,

    Thank you for taking the time to review my application :)

    The first part of the document defines all the functions I need to enter all
    the relevant information about my application. If you are not interested in
    this technical part, you can jump directly to line 92.

    I hope you will enjoy Resumeing it as I had a good time writing it :)

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
            spoken_languages: dict,
            technical_skills: list,
            soft_skills: list):
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
        self.technical_skills = technical_skills
        self.soft_skills = soft_skills

    @staticmethod
    def education(
            degree: str,
            major: str,
            university: str,
            country: str,
            from_: str,
            to_: str,
            main_classes: list):

        list_course = '\n        - '.join(map(str, main_classes))

        output = f"""
        I have a {degree} in {major} from {university}.
        I studied there from {from_} to {to_}.
        During this scholarship here I studied:
        - {list_course}.
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

        list_task = '\n            - '.join(map(str, achievements))

        if to_ == 'Current':
            output = f"""
            I currently work as a {position} at {company}.
            I have been working there since {to_}. Here is a list of some of my achievements:
            - {list_task}.
            """
        else:
            output = f"""
            I worked as a {position} at {company} between {from_} and {to_}.
            Amongst other tasks. Here is a list of some of my achievements:
            - {list_task}.
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
        activity = description
        return activity


####################################################################################################
# PROFILE

Geoffrey_Roig_Deslandes = Resume(
    first_name='Geoffrey',
    last_name='Roig-Deslandes',
    address={
        'Street': 'Saint Charles',
        'Number': '2855A',
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
        'Danish': 'In Progress :)',
        'English': 'Fluent',
        'French': 'Fluent',
        'German': 'Basics'},
    technical_skills=[
        'SQL',
        'Python',
        'Git',
        'AWS',
        'Time Series Forecasting',
        'Data Mining',
        'Supervized learning',
        'Unsupervized learning'
    ],
    soft_skills=[
        'Team player',
        'Creative',
        'Business knowledge',
        'Critical thinking',
        'Desite to learn'
    ]
    )


####################################################################################################
# PROFESSIONAL EXPERIENCE

data_analyst = Resume.experience(
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

bi_analyst = Resume.experience(
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

internship = Resume.experience(
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

analyst = Resume.experience(
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
msc_marketing = Resume.education(
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

m2_economics = Resume.education(
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

bachelor_economics = Resume.education(
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
water_polo_referee = Resume.activities(
    association='Waterpolo Quebec',
    role='Referee',
    city='Montreal',
    country='Canada',
    from_='October 2013',
    to_='Current',
    description="""
    I have been a referee for Waterpolo Quebec October 2013. It taught me to be relentless and to
    learn from my mistakes. It has been one of the greatest challenge I ever met,
    and I proud to say that it helped me be a better person.
    """)

water_polo_player = Resume.activities(
    association='ACC Waterpolo',
    role='Player',
    city='Montreal',
    country='Canada',
    from_='February 2013',
    to_='September 2018',
    description="""
    I played waterpolo at ACC Waterpolo for 5 years, and it helped me developmy team spirit and
    leadership as I also coached the team.
    """)

Ludos = Resume.activities(
    association='Ludos HEC',
    role='Member and Vice-President',
    city='Montreal',
    country='Canada',
    from_='September 2014',
    to_='December 2015',
    description="""
    During my scholarship at HEC I was an active member of Ludos, a student association whom goal is
    to promote the videogame industry to HEC students.
    """)


# END OF MY RESUME
####################################################################################################
####################################################################################################
# STARTING THIS POINT, THERE ARE ONLY COMMANDS THAT ARE NOT RELATED TO MY RESUME.
# FEEL FREE TO TUN THE SCRIP :)
from textwrap import dedent


def bio():
    introduction_part_1 = f"""
    Hi!

    If you chose to run my resume then I guess I caught your attention and you are a little
    bit curious about me :).

    But first things first.

    As you probably know, my name is {Geoffrey_Roig_Deslandes.first_name}.

    What's your name?
    """
    print(dedent(introduction_part_1))

    reader_name = input("Enter your name: ")

    introduction_part_2 = f"""
    Nice to meet you {reader_name}!

    Now a little bit about me.

    I am sure you're wondering why a Canadian Resident is applying for a position in Copenhaguen ?

    Well, after 7 wonderful years in Canada my wife and I wanted to come back closer to our
    families. Furthermore she had a "once in a lifetime opportunity in the city, so we jumped on
    on the occasion, and here I am, applying for this position :)

    But enough about my personal life, I am sure your're also interested my experience.
    """

    to_print = [
        introduction_part_2,
        data_analyst,
        bi_analyst,
        internship,
        analyst,
        msc_marketing,
        m2_economics,
        water_polo_referee,
        water_polo_player,
        Ludos
    ]

    for element in to_print:
        print(dedent(element))
        print('Press any Enter to continue...')
        input()

    conclusion = f"""
    That's it, you know everything about me.

    Of course I would be more than happy to discuss with you {reader_name} about
    my profile and the position. I am sure this will be an interesting conversation for both of us.
    So do not hesitate to contact me by mail at {Geoffrey_Roig_Deslandes.email}.

    Cheers,

    {Geoffrey_Roig_Deslandes.first_name}.
    """
    print(dedent(conclusion))


if __name__ == '__main__':
    bio()
