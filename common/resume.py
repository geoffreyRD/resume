#/python
class Resume:
    """Resume description"""
    def __init__(
            self,
            first_name: str,
            last_name: str,
            address: dict,
            email: str,
            phone_number: int,
            LinkedIn: str,
            GigHub: str,
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
            from_: str,cmd
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

        list_task= ', '.join(map(str, achievements))

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

################################################################################
# PROFILE

################################################################################
# PROFESSIONAL EXPERIENCE

################################################################################
# EDUCATION

################################################################################
# OTHER ACTIVITIES
