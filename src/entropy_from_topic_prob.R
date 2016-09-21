cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/all.corpus/30.TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)

topic_names <- colnames(topic_prob_data, do.NULL = TRUE, prefix = "col")
doc_names <- rownames(topic_prob_data, do.NULL = TRUE, prefix = "row")

topic_names <- topic_names[!topic_names %in% "X"]
#print(topic_names)
#print(doc_names)

# Calculate the entropy of a vector of counts or proportions
# Inputs: Vector of numbers
# Output: Entropy (in bits)
performEntropy <- function(p) {
  # Assumes: p is a numeric vector
  if (sum(as.numeric(p)) == 0) {
    return(0) # Case shows up when calculating conditional
    # entropies
  }
  p <- p/sum(as.numeric(p)) # Normalize so it sums to 1
  p <- p[p > 0] # Discard zero entries (because 0 log 0 = 0)
  H = -sum(p*log(p,base=2))
  return(H)
}



for(topic_index in 1:length(topic_names))
{
  print(topic_index)
  prob_for_topic <- topic_prob_data[,topic_index]
  #print(length(prob_for_topic))
  shannon_entropy <-  performEntropy(prob_for_topic)
  print(shannon_entropy)
  print("---------------")
}


t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))