def makeJaccardEnhancersScript(path, enhancersFileNameListFileName, outputFileName):
    # Make a script that will intersect the enhancers and print the number of lines in each intersection
    enhancersFileNameListFile = open(enhancersFileNameListFileName)
    enhancersFileNameList = enhancersFileNameListFile.readlines()
    enhancersFileNameListFile.close()
    outputFile = open(outputFileName, 'w+')
    for i in range(len(enhancersFileNameList)):
        # Iterate through the enhancer files and get the intersection for each
        fileNameOne = path + enhancersFileNameList[i].strip()
        for j in range(i+1, len(enhancersFileNameList)):
            # Iterate through files for intersection
            fileNameTwo = path + enhancersFileNameList[j].strip()
            intersectfile=fileNameOne + "_" + enhancersFileNameList[j].strip()
            outputFile.write("intersectBed -a " + fileNameOne + " -b " + fileNameTwo + " > " + intersectfile + "\n")
            catfile=path + "temp_cat_file"
            outputFile.write("cat " + fileNameOne + " " + fileNameTwo + " > " + catfile + "\n")
            sortedfile=path + "temp_sorted_file"
            outputFile.write("sort -u -k1,1 -k2,2n -k3,3n " + catfile + " > " + sortedfile + "\n")
            temp_merged_file=path + "temp_merged_file"
            outputFile.write("mergeBed -i " + sortedfile + " > " + temp_merged_file +"\n")
            
            outputFile.write("wc " + temp_merged_file + "\n")
            outputFile.write("wc " + intersectfile + "\n")
    outputFile.close()

if __name__=="__main__":
    import sys
    path = sys.argv[1]
    enhancersFileNameListFileName = sys.argv[2]
    outputFileName = sys.argv[3]
    makeJaccardEnhancersScript(path, enhancersFileNameListFileName, outputFileName)
