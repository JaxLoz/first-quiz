package org.velezreyes.quiz.question6;

public class VendingMachineImpl {

  public static VendingMachine getInstance() {
    return new ControllerVendingMachine();
    
  }
}
