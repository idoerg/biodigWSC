package org.biodig.tags;

public class Point {
	private float x;
	private float y;
	
	public Point(float x, float y) {
		this.x = x;
		this.y = y;
	}
	
	public double getX(){
		return x;
	}
	
	public double getY() {
		return y;
	}
	
	public String toString() {
		return "{ \"x\" : "+x+" , \"y\" : "+y+"}";
	}

}
