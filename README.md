# data-egress-optimization

Hello,

My name is Wyatt and this project is a sample of work I did while working at an inventory management company. Please be aware that all data has been anonymized and randomized to ensure NDA compliance. The sample data does not represent any historical business data and is only used to demonstrate the effectiveness of the coded solution.

The original problem to be solved involved large JSON files being sent to a customer that included transaction data. The issue with this transaction data is that it included "ghost transactions" where an item was incorrectly recorded as being consumed and returned repeatedly, resulting in high data egress and unnecessary convolution.

The task was to aggregate these transactions into single lines.

To explore this project, please take a look at the "Sample Input Data" and compare it against the "Sample Output Data" to get a grasp of the data egress reduction at a glance. Then feel free to review the code noting the various functions resolving the data aggregation. If you would like to take it a step further, you may pull this project and run it on your own machine which will generate another batch of the "Sample Output Data" titled "Test_Output_Data"
