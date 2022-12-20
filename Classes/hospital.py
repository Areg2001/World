class Hospital:
    
    def __init__(self, name: str, count_of_bed: int) -> None:
        self.name = name
        self.count_of_bed = count_of_bed
        self.count_of_patients = 0
    
    def get_count_of_patients(self) -> str:
        return f"Count of patients: {self.count_of_patients}."
    
    def get_count_of_beds(self) -> str:
        return f"Count of beds: {self.count_of_bed}"
    
    def admit_patient(self) -> None:
        if self.count_of_bed > self.count_of_patients:
            self.count_of_patients += 1
            self.count_of_bed -= 1
        
        else:
            print(f"Sorry, we have no free bed.")    
    
    def discharge_patient(self) -> None:
        self.count_of_patients -= 1
        self.count_of_bed += 1
    
    def add_bed(self) -> None:
        self.count_of_bed += 1
    
    def remove_bed(self) -> None:
        self.count_of_bed -= 1

    
        
    
    
                
        
    
        