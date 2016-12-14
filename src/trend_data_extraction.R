cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))