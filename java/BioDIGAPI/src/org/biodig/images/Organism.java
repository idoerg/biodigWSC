package org.biodig.images;
public class Organism
	{
		public Organism(String abbreviation, String genus, String commonName,
			String species, int id) {
		super();
		this.abbreviation = abbreviation;
		this.genus = genus;
		this.commonName = commonName;
		this.species = species;
		this.id = id;
	}

		private String abbreviation;
		private String genus;
		private String commonName;
		private String species;
		private int id;

		public String getAbbreviation() {
			return abbreviation;
		}

		public void setAbbreviation(String abbreviation) {
			this.abbreviation = abbreviation;
		}

		public String getGenus() {
			return genus;
		}

		public void setGenus(String genus) {
			this.genus = genus;
		}

		public String getCommonName() {
			return commonName;
		}

		public void setCommonName(String commonName) {
			this.commonName = commonName;
		}

		public String getSpecies() {
			return species;
		}

		public void setSpecies(String species) {
			this.species = species;
		}

		public int getId() {
			return id;
		}

		public void setId(int id) {
			this.id = id;
		}

		@Override
		public String toString() {
			return "organisms \n [abbreviation=" + abbreviation + ",\n genus="
					+ genus + ",\n commonName=" + commonName + ",\n species="
					+ species + ",\n id=" + id + "]";
		}
	}
