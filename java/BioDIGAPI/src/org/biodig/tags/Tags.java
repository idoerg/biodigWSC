package org.biodig.tags;

import java.util.Arrays;


import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.google.gson.stream.JsonReader;


public class Tags {
	private int id;
	private String name;
	private String dateCreated;
	private int[] color;
	private Point[] points;

	/*
	 * Constructor for GET request
	 */
	
	public Tags (int id, String name, String dateCreated,int[] color, Point[] points) {
		this.id = id;
		this.name = name;
		this.dateCreated = dateCreated;
		this.color = color;
		this.points = points;
	}

	public int getID() {
		return id;
	}

	public void setID(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getDateCreated() {
		return dateCreated;
	}

	public void setDateCreated(String dateCreated) {
		this.dateCreated = dateCreated;
	}

	public int[] getColor() {
		return color;
	}

	public void setColor(int[] color) {
		this.color = color;
	}

	public Point[] getPoint() {
		return points;
	}

	public void setPoint(Point[] points) {
		this.points = points;
	}

	@Override
	public String toString() {
		return "Tags ["
				+ "\n"+"id=" + id + ", "
				+ "\n"+"name=" + name + ", "
				+ (dateCreated != null ? "\n"+"dateCreated=" + dateCreated + ", "
						: "")
				+ "\n"+"color=" + Arrays.toString(color) + ", "
				+ "\n"+"points=" + Arrays.toString(points)
				+ "\n"+"]";
	}

}
