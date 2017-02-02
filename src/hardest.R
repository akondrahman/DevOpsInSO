cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

content_file <-  "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/ForReproc/FullQAndAContent.csv"
content_data <- read.csv(content_file)

topic_prob_file <- "/Users/akond/Documents/AkondOneDrive/OneDrive/StackOverflowProject/DevOpsInSO/output/rq1/you_are_never_done/_TopicProb.csv"
topic_prob_data <- read.csv(topic_prob_file)

topic_names <- colnames(topic_prob_data, do.NULL = TRUE, prefix = "col")
doc_names <- rownames(topic_prob_data, do.NULL = TRUE, prefix = "row")

topic_names <- topic_names[!topic_names %in% "X"]
#print(topic_names)
#print(doc_names)
len_doc_names <- length(doc_names)
len_top_names <- length(topic_names)
dic_topics <- vector(mode="list", length=len_doc_names)
names(dic_topics) <- doc_names
###threshold 
topic_prob_cutoff <- 0.10
for(doc_ind in 2:len_doc_names)
{
  
  topics_for_this_doc <- vector(mode="numeric", length=len_top_names+1)
  dom_topic_for_this_doc <- rep(0, len_top_names+1)
  for(topic_ind in 1:len_top_names+1)
  {
    topic_prob_for_doc <- topic_prob_data[doc_ind, topic_ind]
    topics_for_this_doc[topic_ind] <- topic_prob_for_doc
  }
  #max_topic_prob <-  max(topics_for_this_doc)
  #print(max_topic_prob)
  index_with_max_prob <- which(topics_for_this_doc >= topic_prob_cutoff)
  #print("-----")
  #print(index_with_max_prob)
  dom_topic_for_this_doc[index_with_max_prob] <- 1
  #print(dom_topic_for_this_doc)
  dic_topics[[doc_ind]] <- dom_topic_for_this_doc
  #print("-----")  
}
len_dic_topic <- length(dic_topics)        ## get the count of all questions in the corpus 

aa_vector    <-  content_data$AcceptedAnswerId   ## get accepted answer IDs from content file 
#print(aa_vector)
#aa_vector    <- as.numeric(aa_vector)    ## convert to number 

for(top_inex in 1:len_top_names+1)
{

  ### counter_ for all questions 
  counter_ <- 0 
  
  ### counter for questions for this topic 
  q_count_topic <- 0 
  
  ### counter for aa questions for this topic 
  aa_q_count_topic <- 0 
  
  ### counter for naa questions for this topic 
  naa_q_count_topic <- 0   
  
  print("#########################")
  print("Topic #")
  print(top_inex-1)
  for(doc_index in 2:len_dic_topic)
  {
    counter_ <- counter_ + 1 
    tmp_ <-  dic_topics[[doc_index]][top_inex]
    if(tmp_==1)
    {
      q_count_topic <- q_count_topic + 1
      tmp_aa_value <- aa_vector[counter_]
      if ( (tmp_aa_value !="") && (!is.na(tmp_aa_value)) )
      {
        aa_q_count_topic <-   aa_q_count_topic  + 1
        #print("lol")
      }
      else
      {
        #print(tmp_aa_value)
        naa_q_count_topic <-   naa_q_count_topic + 1
      }
    }
  }
  
  print("***Total questions in this topic***")
  print(q_count_topic)
  #print("***Total questions with aa in this topic***")
  #print(aa_q_count_topic)  
  #print("***Total questions with naa in this topic***")
  #print(naa_q_count_topic)    
  hardness <- (( naa_q_count_topic - aa_q_count_topic) / q_count_topic ) * 100
  print("***Hardness this topic***")
  print(hardness)      
}

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))