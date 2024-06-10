package org.velezreyes.quiz.question6;

public class ControllerVendingMachine implements VendingMachine {
    
    private int Quarter;
    private String DrinksAvailable[] = {"ScootCola", "KarenTea"};
    
    public ControllerVendingMachine (){
        this.Quarter = 0;
    }
    

    @Override
    public void insertQuarter() {
        Quarter+=25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        
        ClassDrink CD = null;
        String nameDrink = name;
        boolean exists = false;
        
        for (String DrinksAvailable1 : this.DrinksAvailable) {
            if (nameDrink.equals(DrinksAvailable1)) {
                exists = true;
                break;
            }
        }
        
        
        if (exists){
            
        }else{
            throw new UnknownDrinkException();
        }
          
        return CD;
    }

    
    
}
