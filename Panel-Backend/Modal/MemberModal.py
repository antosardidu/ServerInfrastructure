class member(object):
    # def __init__(self, userName = None, email = None, bank = None, phoneNumber = None, bankAccNumber = None, bankAccName = None, referral = None):
    #   self.userName = userName
    #   self.email = email
    #   self.bank = bank
    #   self.phoneNumber = phoneNumber
    #   self.bankAccNumber = bankAccNumber
    #   self.bankAccName = bankAccName
    #   self.referral = referral
    
    def __setMember__(self, userName: str, email:str, bank:str, phoneNumber:str, bankAccNumber:str, bankAccName:str, referral:str):
      self.userName = userName
      self.email = email
      self.bank = bank
      self.phoneNumber = phoneNumber
      self.bankAccNumber = bankAccNumber
      self.bankAccName = bankAccName
      self.referral = referral

    def __getMember__(self):
        out = self.__dict__
        return(out)