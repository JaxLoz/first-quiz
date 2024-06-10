package org.velezreyes.quiz.question6;

public class ClassDrink implements Drink {
    
    private String drinkName;
    private boolean fizzy;
    
    public ClassDrink (){
        this.drinkName = "";
        this.fizzy = false;
    }
    
    public void setFizzy (boolean fizzy){
        this.fizzy = fizzy;
    }
    
    public void setDrinkName (String nameDrink){
        this.drinkName = nameDrink;
    }

    @Override
    public String getName() {
        return this.drinkName;
    }

    @Override
    public boolean isFizzy() {
        return this.fizzy;
    }
    
}
