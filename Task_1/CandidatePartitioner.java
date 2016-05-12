import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.Partitioner;
import org.apache.hadoop.io.Text;

public class CandidatePartitioner implements Partitioner<Text, Text> {

	@Override
	public int getPartition(Text key, Text value, int numReduceTasks) {
		if (numReduceTasks==0)
			return 0;
		else if(key.toString().equalsIgnoreCase("other"))
			return 0;
		else if(key.toString().equalsIgnoreCase("clinton"))
			return 1 % numReduceTasks;
		else if(key.toString().equalsIgnoreCase("trump"))
			return 2 % numReduceTasks;
		else if(key.toString().equalsIgnoreCase("sanders"))
			return 3 % numReduceTasks;
		else if(key.toString().equalsIgnoreCase("cruz"))
			return 4 % numReduceTasks;
		else if(key.toString().equalsIgnoreCase("kasich"))
			return 5 % numReduceTasks;
		else if(key.toString().equalsIgnoreCase("rubio"))
			return 6 % numReduceTasks;
		else
			return 0;
	}

	@Override
	public void configure(JobConf arg0) {
		// TODO Auto-generated method stub

	}
}
