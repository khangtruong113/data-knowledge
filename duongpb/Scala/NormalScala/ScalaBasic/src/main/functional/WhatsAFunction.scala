package main.functional

class WhatsAFunction extends App {

  //DREAM: use functions as first class elements

  //problem : OOP(everything is object)

  val doubler = new MyFunction[Int, Int]{
    override def apply(element: Int): Int = element * 2
  }

  print(doubler(2))
  //we can call double - an instance of class can be call like a function

  //function types = Function1[A, B]

  val stringToIntConverter = new Function1[String, Int]{
    override def apply(string: String): Int = string.toInt
  }

  println(stringToIntConverter("3") + 4)

  val adder: ((Int, Int)=>Int) = new Function2[Int, Int, Int]{
    override def apply(a: Int, b: Int): Int = a + b

    //. this is syntaxtic sugar for this function : Function type : Function2[A, B, Result] === (A, B) => R
  }

  // ALL SCALA FUNCTIONS ARE OBJECTS

  
}

class Action {
  def execute(element: Int): String = ???
}

trait MyFunction[A, B]{
  def apply(element: A): B
}
