object DefaultArg extends App{
  def trFact(n: Int, acc: Int = 1): Int =
    if (n <= 1) acc
    else trFact(n - 1, n * acc)

  val fact10 = trFact(10)

  // scala allow to pass default parameter for    function, we can override the value by fill in the declaration for it afterward

  /**
   * 1. pass in every leading arg
   * 2. namne the arguments
   */
//  for eg:
    def savePivture(format: String = "jpg", width: Int = 1920, height: Int = 1080): Unit = println("hello")

  savePivture(height = 600, width = 43243, format = "bmb")
}
