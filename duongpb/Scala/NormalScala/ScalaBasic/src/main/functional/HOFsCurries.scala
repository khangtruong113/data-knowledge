//package main.functional
////higher order function and curries
//object HOFsCurries extends App {
//  val superFunction: (Int, (String, (Int => Boolean)) => Int) => (Int => Int) = null
//  // higher order function is when it takes a function as a parameter or it return a function as a result
//
//  // such function as map, flatmap, filter in MyList
//
//  // function that applies a function n times over a value "x"
//
//  // nTimes(f, n, x)
//  // nTime(f, 3, x) = f(f(f(x)))
//  // nTimes(f, n, x) = f(f(...f(x))) = nTimes(f, n-1, f(x)) -> recursive
//  def nTimes(f: Int => Int, n: Int, x: Int): Int =
//    if (n <= 0) x
//    else nTimes(f, n - 1, f(x))
//
//  val plusOne = (x: Int) => x + 1
//
//  println(nTimes(plusOne, 10, 1))
//
//  // nTimesBetter(f,n) = x=> f(f(f...(x)))
//  //increment10 = ntb(plusOne, 10) = x=> plusOne(plusOne...(x))
//  //val y = increment10(1)
//  def nTimesBetter(f: Int => Int, n: Int): (Int => Int) =
//    if(n <= 0)(x:Int) => x
//    else (x: Int) => nTimesBetter(f, n-1)(f(x))
//
//    val plus10 = nTimesBetter((plusOne, 10))
//    println(plus10(1))
//
//    //curreid functions
//    val superAdder: Int => (Int => Int) = (x: Int) => (y: Int) => x +y
//    val add3 = superAdder(3) //lambda for y = 3 + y
//
////  println(add3(10)) // same to superAdder(3)(5)
//    print(superAdder(plusOne(10)))
//
//  //function with multiple parameter lists
//  def curriedFormatter(c: String)(x: Double): String = c.format(x)
//
//  val standardFormat: (Double => String) = curriedFormatter("4.2f")
//  val preciseFormat: (Double => String) = curriedFormatter("10.8f")
//
//}
