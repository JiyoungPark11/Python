#From the output directory of the OrthoFinder, under the forlder "Orthogroups" import the file Orthogroups.GeneCount.tsv into data frame
library(readr)
Orthogroups_GeneCount <- read_delim("Orthogroups.GeneCount.tsv", 
                                    delim = "\t", escape_double = FALSE, 
                                    trim_ws = TRUE)
# View header
colnames(Orthogroups_GeneCount)

#filter Species-specific_orthogroup, using first letter of genus and first 2 letters of species 
Mbi_orthogroup <- subset(Orthogroups_GeneCount, Apis_mellifera == Total)

# Subset corresponding orthogroup number
Mbi_OG_ids <- (subset(Mbi_orthogroup, select = 'Orthogroup'))

# Append .fa to each entry in the Orthogroup column
Mbi_OG_ids$Orthogroup <- paste0(Mbi_OG_ids$Orthogroup, ".fa")

# Write the subset to a text file
write.table(Mbi_OG_ids, file = "Mbi_OG_id.txt", row.names = FALSE, col.names = FALSE, quote = FALSE, sep = "\t")
