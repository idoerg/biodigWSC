package org.biodig.tags;

import java.util.Arrays;


public class test {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		TagAPI newBioDIG = new TagAPI("http://192.168.88.143/api/");
		
		// Test GET for Tag api
		//Tags testTag = newBioDIG.getTAG(1);
		//System.out.println(testTag.toString());
				
		Point point1 = new Point(170,120);
		Point point2 = new Point(220,210);
		
		TagQuery newQuery = new TagQuery();
		newQuery.addPoints(point1, point2);
		newQuery.addColor(20,20,20);
		newQuery.addName("hihihi");
		
		//newBioDIG.editTAG(1,newQuery);
				
		newBioDIG.deleteTAG(1);
		
		// Test GET for Tag api
		//testTag = newBioDIG.getTAG(1);
		//System.out.println(testTag.toString());
		

	}

}
