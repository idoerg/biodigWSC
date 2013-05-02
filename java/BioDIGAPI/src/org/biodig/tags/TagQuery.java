package org.biodig.tags;

import java.util.Arrays;

import javax.ws.rs.core.MultivaluedMap;


import com.sun.jersey.core.util.MultivaluedMapImpl;

public class TagQuery{
	MultivaluedMap params;
	private int id,tagGroupId,tagId,organismId;
	private Point[] points;
	private Color color;
	private String name,uniquename;
	
	public TagQuery(){
		this.params = new MultivaluedMapImpl();
		this.id = -1;
		this.tagGroupId = -1;
		this.tagId = -1;
		this.organismId = -1;
		this.color = null;
		this.points = null;
		this.name = "";
		this.uniquename = "";
	}
	
	public void addId(int id) {
		this.id = id;
	}
	
	public void addTagGroupId(int tagGroupId) {
		this.tagGroupId = tagGroupId;
	}
	
	public void addTagId(int id) {
		this.tagId = id;
	}
	
	public void addOrganismId(int id) {
		this.organismId = id;
	}
	public void addPoints(Point[] points) {
		this.points = points;
	}
	
	public void addPoints(Point firstPoint, Point secondPoint) {
		Point[] newPoint = new Point[]{firstPoint,secondPoint};
		this.points = newPoint;
	}
	
	public void addColor(Color color) {
		this.color = color;
	}
	
	public void addColor(int red,int green, int blue) {
		Color newColor = new Color(red,green,blue);
		this.color = newColor;
	}
	
	public void addName(String name) {
		this.name = name;
	}
	
	public void addUniqueName(String name) {
		this.uniquename = name;
	}
	
	public MultivaluedMap getQuery() {
		if(id != -1)
			params.add("id", Integer.toString(id));
		if(tagGroupId != -1)
			params.add("tagGroupId", Integer.toString(tagGroupId));
		if(tagId != -1)
			params.add("tagId", Integer.toString(tagId));
		if(organismId != -1)
			params.add("organismId", Integer.toString(organismId));
		if(points != null)
			params.add("points", Arrays.toString(points));
		if(color != null)
			params.add("color", color.toString());
		if(!name.equals(""))
			params.add("name", name);
		if(!uniquename.equals(""))
			params.add("uniquename", uniquename);
		
		System.out.println(params.toString());
		
		return params;
	}
}
