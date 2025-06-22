package com.example.AI.Payloads.Requests;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import java.math.BigDecimal;

@AllArgsConstructor
@Getter
@Setter
public class RecommendationRequest {
    private BigDecimal minPrice;
    private BigDecimal maxPrice;
    private String city;
    private Integer rooms;
}
