
class Registration:

    @staticmethod
    def register_user(email, password, first_name, last_name):
        if ("@" in email) and (len(password) > 6):
            return Profile(first_name, last_name)


class FbModel:
    def __init__(self, profile_picture, cover_picture):
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture
    
    def get_profile_pictrue_url(self):
        return "wwww.fb.com/profile/"+self.profile_picture
    
    def get_cover_pictrue_url(self):
        return "wwww.fb.com/cover/"+self.cover_picture

class Profile(FbModel):
    
    def __init__(self,first_name, last_name, profile_picture=None, cover_picture=None):
        super().__init__(profile_picture, cover_picture)
        self.first_name = first_name
        self.last_name = last_name
    @property
    def get_full_name(self):
        return self.first_name+" - "+self.last_name

    def __str__(self):
        return self.first_name+" - "+self.last_name+" - "+self.get_profile_pictrue_url()+" - "+self.get_cover_pictrue_url()

class Page(FbModel):
    def __init__(self, name, profile_picture, cover_picture, followers=0):
        super().__init__(profile_picture, cover_picture)
        self.name = name
        self.followers = followers
    
    def get_info(self):
        return {
            'name':self.name,
            'followers':self.followers
        }

    def __add__(self,other):
        return self.name+" - "+other.name+" - "+" Total Followers: "+str(self.followers+other.followers)
    
    def __sub__(self,other):
        return self.name+" - "+other.name+" - "+" Total Followers Sub: "+str(self.followers-other.followers)



#user1 = Profile(first_name="Astghik", last_name="Tonoyan", profile_picture="astghik.jpeg", cover_picture="astghik_tonoyan.jpeg")
#user1 =

#ArmGovPage = Page("Arm Gov", 'armgov.jpeg','armgov_cover.jpeg',4500)

#print(ArmGovPage-codeTubesPage)

myProfile = Registration.register_user("astghik@mail.com", "Passwrod123!", "Astghik", "Tonoyan")
print(myProfile.get_full_name)
